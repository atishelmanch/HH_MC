#!/bin/bash
voms-proxy-init --voms cms --valid 168:00
source /cvmfs/cms.cern.ch/crab3/crab.sh
cmsenv
crab submit -c Crab_File.py
crab status