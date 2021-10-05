#!/bin/sh
cd CMSSW_9_3_8/src
cmsenv 
seed=$(date +%s)
cmsDriver.py Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-00580.py --fileout file:kl_0_kt_1_100Events.root --mc --eventcontent GENRAW --datatier LHE --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename kl_0_kt_1_100Events_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed}%100)" -n 100
cmsRun kl_0_kt_1_100Events_cfg.py 