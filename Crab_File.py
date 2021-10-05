from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
 
config.General.requestName = 'abe_HH_MC'
config.General.workArea = 'abe_HH_MC_crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False
 
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '/afs/cern.ch/work/a/atishelm/private/HH_MC/Production/CMSSW_9_3_8/src/newgridpack_test_cfg.py'
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 8000
 
config.Data.outputPrimaryDataset = 'abe_HH_MC_PrimaryDataset'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 25
NJOBS = 200  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/atishelm/HH_MC/'
config.Data.publication = True
config.Data.outputDatasetTag = 'abe_HH_MC_outputDatasetTag'
 
config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'
