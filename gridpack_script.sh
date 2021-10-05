#!/bin/sh
#git clone git@github.com:cms-sw/genproductions.git genproductions
cd genproductions/bin/MadGraph5_aMCatNLO/
. gridpack_generation.sh kl_0_kt_1 cards/production/2017/13TeV/GF_HH_benchmarks/kl_0_kt_1
. gridpack_generation.sh BulkGraviton_hh_GF_HH_narrow_M320 cards/production/2017/13TeV/exo_diboson/Spin-2/BulkGraviton_hh_narrow/BulkGraviton_hh_GF_HH_narrow_M320
