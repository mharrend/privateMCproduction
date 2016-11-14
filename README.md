# privateMCproduction for HC 2016
Private MC production for CMS


## Note: HC2016 settings
**Note**
This configuration is using the settings which were used for the HC2016 production. 

## Requirements
* CMSSW environment
* Sufficient storage space -- either local or on a grid site
* Optional access to grid and crab scripts



## Receipt for LHEGEN level production
1. Clone this repository to any folder
1. Open the trancheprivateproduction.sh script contained in the folder
1. Adjust the first four parameters until "Do not change anything
behind this line" according to your local setup.
  1. NUMBEREVENTS: Defines how many events you want to produce
  1. WORKDIR: Defines in which directory CMSSW installation is set up and where in local production events are stored
  1. GRIDPACKLOC: Defines which gridpack is used, you can choose the Powheg ttbar, semileptonic decay or Powheg ttbar, dileptonic decay gridpack. 
  1. USECRAB: False means local production, True results in crab submission
1. Additional step for crab submission: Check and modify crabconfig_draft.py script:
  1. config.Site.storageSite: Set your grid storage site, e.g. 'T2_DE_DESY' for german users
  1. config.User.voGroup: If you a non-german user, you should comment out this section.
1. Start the production via ./trancheprivateproduction.sh

## Notes
* The current settings are optimized for a grid submission during which you should produce roughly 400k events per day.
* If you would like to use other gridpacks, contact me first since the python config file has to be updated then.

##  Overview of files in framework
* trancheprivateproduction.sh: Main steering script. Only script which should be edited by user.
* run_generic_tarball_cvmfs.sh: Generic script to produce LHE events out of gridpacks
* pythonLHEGEN_cfg_draft.py: CMSSW python run script
* crabconfig_draft.py: Crab submission script, can be adjusted by user.
