from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "privateMCProductionAODSIMStep1"
config.General.workArea = 'crab_privateMCProduction'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'pythonLHEGEN_cfg.py'
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.outputPrimaryDataset = 'privateMCProductionAODSIMStep1'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1200
config.Data.totalUnits = #NUMBEREVENTS#
config.Data.publication = False
config.Data.outputDatasetTag = 'eventAODSIMStep1'

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'

config.section_("User")
config.User.voGroup = "dcms"

