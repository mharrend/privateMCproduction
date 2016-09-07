#!/bin/bash

# Define number of events
export NUMBEREVENTS=10

# Define workdir
export WORKDIR=/nfs/dust/cms/user/mharrend/trancheprivateproduction/GenSimAODSim8

# Define location of GenSim samples, warning make sure that you run only one time on the same folder since otherwise we will produce two times the events.
# Furthermore, you have to give an absolute path name
export GENSIMLOC=/pnfs/desy.de/cms/tier2/store/user/husemann/privateMCProductionLHEGEN/eventLHEGEN/160826_060732
# export GRIDPACKLOC=/afs/cern.ch/work/m/mharrend/public/ttHtranche3/TTTo2L2Nu_hvq_ttHtranche3.tgz

# Use crab for grid submitting, adjust crabconfig.py accordingly beforehand
#export USECRAB="True" Does not work yet, needs some adjustments
export USECRAB="False"

######### Do not change anything behind this line ###############


export STARTDIR=`pwd`
echo "Start dir was:"
echo $STARTDIR

echo "Workdir set is:" 
echo $WORKDIR
mkdir -p $WORKDIR
echo "Created workdir"
cd $WORKDIR
echo "Changed into workdir"

echo "Install CMSSW in workdir"
source /cvmfs/cms.cern.ch/cmsset_default.sh 
scram project CMSSW_8_0_14
cd CMSSW_8_0_14/src
eval `scramv1 runtime -sh`
echo "Loaded CMSSW_8_0_14"

echo "Create list with files to process"
find $GENSIMLOC -name "eventLHEGEN-output_*.root" -exec echo "'file:"{}"'," \; > filelist.txt

echo "Change file list in python config to"
echo "##########"
echo $(cat filelist.txt)
echo "##########"
sed -e "s|#INPUTFILES#|"$(cat filelist.txt)"|g" $STARTDIR/GenSimAODSim_step1_cfg_draft.py > ./GenSimAODSim_step1_cfg_filesInserted.py

echo "Change number of events in python config to"
echo $NUMBEREVENTS
sed -e "s/#NUMBEREVENTS#/${NUMBEREVENTS}/g" GenSimAODSim_step1_cfg_filesInserted.py > ./GenSimAODSim_step1_cfg_eventsInserted.py
sed -e "s/#NUMBEREVENTS#/${NUMBEREVENTS}/g" $STARTDIR/GenSimAODSim_step2_cfg_draft.py > ./GenSimAODSim_step2_cfg_eventsInserted.py

if [ $USECRAB = "True" ]; then
	echo "Will use crab submission, adjust crabconfig.py accordingly if problems arise"

        echo "Scram b and start of LHEGEN production"
	scram b -j 4
	
	echo "Load crab environment, grid environment should be loaded manually in advance if necessary"
	#source /cvmfs/cms.cern.ch/crab3/crab.sh

	echo "Change number of events in crab config to"
	echo $NUMBEREVENTS
	echo " and copy crabconfig.py to workdir"
	sed -e "s/#NUMBEREVENTS#/${NUMBEREVENTS}/g" $STARTDIR/crabconfig_draft.py > ./crabconfig.py

        echo "Scram b and start of LHEGEN production"
        scram b -j 4

	echo "Submit crab jobs"
	#crab submit crabconfig.py

	echo "Finished with crab submission, check job status manually"
else
	echo "Will do local production using cmsRun"

	echo "Scram b and start of LHEGEN production"
	scram b -j 4

	echo "Starting first of two steps"
	cmsRun GenSimAODSim_step1_cfg_eventsInserted.py
	echo "Finished step1 of local production using cmsRun"

	echo "Starting second of two steps"
	cmsRun GenSimAODSim_step2_cfg_eventsInserted.py
	echo "Finished local production using cmsRun"
fi
