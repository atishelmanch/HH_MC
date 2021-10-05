# #!/bin/sh
# export SCRAM_ARCH=slc6_amd64_gcc700
# source /cvmfs/cms.cern.ch/cmsset_default.sh
# # export SCRAM_ARCH=slc7_amd64_gcc700
# # source /cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw-patch/CMSSW_10_2_13_patch1
# if [ -r CMSSW_10_2_13_patch1/src ] ; 
# then 
#     echo "release CMSSW_10_2_13_patch1 already exists"
# else
#     scram p CMSSW CMSSW_10_2_13_patch1
# fi
# cd CMSSW_10_2_13_patch1/src
# eval `scram runtime -sh`


#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_6/src ] ; then 
 echo release CMSSW_10_2_6 already exists
else
scram p CMSSW CMSSW_10_2_6
fi
cd CMSSW_10_2_6/src
eval `scram runtime -sh`


# SCRAM warning: You are trying to compile/build for architecture slc6_amd64_gcc700 on SLC7 OS which might not work.
# If you know this SCRAM_ARCH/OS combination works then please first run 'scram build --ignore-arch'.
#