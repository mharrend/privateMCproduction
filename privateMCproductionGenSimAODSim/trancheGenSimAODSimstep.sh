#!/bin/bash

# Define number of events
export NUMBEREVENTS=12000

# Define workdir
#export WORKDIR=`pwd`
export WORKDIR=/nfs/dust/cms/user/mharrend/trancheprivateproduction/test8

# Define location of GenSim samples, warning make sure that you run only one time on the same folder since otherwise we will produce two times the events.
# You will get an error message if you try to reuse some of the input files, so please make sure that you start this production only after all GenSim events are produced.
# Furthermore, you have to give an absolute path name
export GENSIMLOC=/pnfs/desy.de/cms/tier2/store/user/husemann/privateMCProductionLHEGEN/eventLHEGEN/160822_162317


# Use crab for grid submitting, adjust crabconfig.py accordingly beforehand
# Use of crab is necessary so far
export USECRAB="True"

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

echo "Make sure that GenSim event files are not used twice by checking if a GenSimAlreadyUsed.txt file exists in one of the subfolders"
echo "If file is found, production will not be started. Please contact Andrej or Marco to clarify if this warning is unexpected, e.g. you did not produce DR event files yet."
export ALREADYUSED=`find $GENSIMLOC -name "GenSimAlreadyUsed.txt" -print`
if [ -z "$ALREADYUSED" ]; then
   echo $ALREADYUSED
   echo "Production can go on"
else
    echo "GenSimAlreadyUsed.txt file was found. Since GenSim events were already used, production will not be started. Contact Andrej and Marco if you have questions."
    exit -1
fi

echo "Create file for blocking of second production using same input files"
touch $GENSIMLOC/GenSimAlreadyUsed.txt


echo "Make sure that GenSim event files are not used twice by checking if a GenSimAlreadyUsed.txt file exists in repository folder"
echo "If file is found, production will not be started. Please contact Andrej or Marco to clarify if this warning is unexpected, e.g. you did not produce DR event files yet."
export ALREADYUSED=`find . -name "GenSimAlreadyUsed.txt" -print`
if [ -z "$ALREADYUSED" ]; then
   echo $ALREADYUSED
   echo "Production can go on"
else
    echo "GenSimAlreadyUsed.txt file was found. Since GenSim events were already used, production will not be started. Contact Andrej and Marco if you have questions."
    echo "Check GenSimAlreadyUsed.txt file in this folder. If you want to give another GENSIMLOC than you used before it is safe to delete this file, but please make sure that nobody else used this GENSIMLOC before."
    exit -1
fi

echo "Create file for blocking of second production using same input files"
touch $STARTDIR/GenSimAlreadyUsed.txt
echo $GENSIMLOC > $STARTDIR/GenSimAlreadyUsed.txt

echo "Create list with files to process"
find $GENSIMLOC -name "eventLHEGEN-output_*.root" -exec echo "'file:"{}"'," \; > filelist_draft.txt

echo "Change file list in python config to"
# Remove new lines in filelist
cat filelist_draft.txt | tr -d "\n" > filelist.txt
echo "##########"
cat filelist.txt
echo
echo "##########"
head -c -1 -q  $STARTDIR/GenSimAODSim_step1_cfg_draft_part1.py filelist.txt $STARTDIR/GenSimAODSim_step1_cfg_draft_part2.py > ./GenSimAODSim_step1_cfg_filesInserted.py


echo "Change number of events in python config to"
echo $NUMBEREVENTS
sed -e "s/#NUMBEREVENTS#/${NUMBEREVENTS}/g" GenSimAODSim_step1_cfg_filesInserted.py > ./GenSimAODSim_step1_cfg.py
sed -e "s/#NUMBEREVENTS#/${NUMBEREVENTS}/g" $STARTDIR/GenSimAODSim_step2_cfg_draft.py > ./GenSimAODSim_step2_cfg.py
sed -e "s/#NUMBEREVENTS#/${NUMBEREVENTS}/g" $STARTDIR/GenSimAODSim_step3_cfg_draft.py > ./GenSimAODSim_step3_cfg.py

if [ $USECRAB = "True" ]; then
	echo "Will use crab submission, adjust crabconfig.py accordingly if problems arise"

        echo "Scram b and start of GenSim to AODSim to MiniAOD production"
	scram b -j 4

	echo "Load crab environment, grid environment should be loaded manually in advance if necessary"
	source /cvmfs/cms.cern.ch/crab3/crab.sh

	echo "Change number of events in crab config to"
	echo $NUMBEREVENTS
	echo " and copy crabconfig.py to workdir"
	sed -e "s/#NUMBEREVENTS#/${NUMBEREVENTS}/g" $STARTDIR/crabconfig_draft.py > ./crabconfig.py

        echo "Scram b and start of GenSim to AODSim to MiniAOD production"
        scram b -j 4

	echo "Submit crab jobs"
	crab submit crabconfig.py

	echo "Finished with crab submission, check job status manually"
	echo "In the end you should get MiniAOD files."
else
	echo "Local production using cmsRun is not supported."
	exit -1
fi
