#!/usr/bin/env python
# 7 February 2019
# Abe Tishelman-Charny 
# Updated 31 May 2019 for HH MC 
from ROOT import * 
import array as arr 
import numpy as np
from NormSigma_Plotter_Config import * 
import subprocess
#import ROOT
gROOT.SetBatch(True)
from DataFormats.FWLite import Handle, Runs, Lumis, Events  #, ChainEvent 
import sys
import os 
from os import listdir
print '.'
print 'Plotting HH Variables'
print '.'
ol = '/eos/user/a/atishelm/www/HH_MC/'
for iv,v in enumerate(vs):
    print 'Plotting variable ', iv, ': ',v[0]
    # For each directory 
    for dn,d in enumerate(d):
        direc = d[0] # full path of directory 
        rd = d[1] # direc path with root://cmsxrootd.fnal.gov/ prefix for 'Events' module  
        path_ends = [fp for fp in listdir(direc) if 'inLHE' not in fp]  # Save paths of non-LHE files
        #path_ends = [fp for fp in listdir(direc)]  # Save paths of non-LHE files
        paths = []
        for pa in path_ends:
            tmp_path = rd + pa
            paths.append(tmp_path)
        # print '  Creating histos for file(s) of type: ',DID 
        # Get chosen particles to plot and number of them 
        pparams = []
        pparams = get_pparams(ptp)
        #pparams = get_pparams(ch,ptp) #particle parameters 
        # print 'pparams = ',pparams 
        # For each file in directory
        # print 'paths = ',paths 
        ext_kl = float(5) 
        third_k = float(20)
        third_k_str = str(third_k)
        ext_kl_str = str(ext_kl)
        h_ext = TH1F('h_ext', 'Extrapolated #kappa_{#lambda} = ' + str(ext_kl) , v[1], v[2], v[3])
        h_ext.Sumw2(1)
        h_ext.GetXaxis().SetRangeUser(250,1000)
        h_os = TH1F('h_os', 'One Sample #kappa_{#lambda} = ' + str(ext_kl) , v[1], v[2], v[3])
        h_os.Sumw2(1)
        h_os.GetXaxis().SetTitle('m_{HH}')
        h_os.GetXaxis().SetRangeUser(250,1000)
        h_os.GetYaxis().SetTitle('Entries')
        #h_tmp.SetMinimum(-500)
        for ip,path in enumerate(paths):
            print '    Processing file ', ip+1, ': ',path 
            kl = path.split('/')[-1].split('_')[1]
            print'kl = ',kl 
            # weight = 0
            TotXSec = 0
            # weight_0 = (-ext_kl*ext_kl / (third_k*(third_k-1))) + ((ext_kl*ext_kl) / (third_k - 1)) + 1 - (ext_kl*third_k)/(third_k - 1) + (ext_kl / (third_k*(third_k-1)))
            # weight_1 = (-ext_kl*ext_kl / (third_k - 1)) + ext_kl*third_k / (third_k - 1)
            # weight_third = (ext_kl*ext_kl / (third_k*(third_k-1))) - (ext_kl / (third_k*(third_k-1)))
            # print'.'
            # print'weight 0 =',weight_0  
            # print'weight 1 =',weight_1  
            # print'weight third =',weight_third  
            # print'.'
            # b = 
            # i = 
            # sigma_k = ext_kl*ext_kl*t + b + ext_kl*i 
            if (kl == "0"): 
                #TotXSec = 0.02823 # Note: I actually made klambda 0.0001 for this because there were problems when setting it to zero. Maybe this effects output? 
                TotXSec = 0.02828 # Note: I actually made klambda 0.0001 for this because there were problems when setting it to zero. Maybe this effects output? 
            elif (kl == "1"): 
                TotXSec = 0.01332
                # TotXSec = 0.01332
            elif (kl == "5"):
                TotXSec = 0.03223
                # TotXSec = 0.03224
            elif (kl == "20"):
                TotXSec = 1.222
                # TotXSec = 1.224
            elif (kl == "245"):
                TotXSec = 0.005642
            else:
                print'I don\'t know what to do with kl = ',str(kl)
                print'Exiting'
                exit(0)
            events = Events(path) # needs to be file with root prefix 
            xbins = v[1]
            xmin = v[2]
            xmax = v[3]
            db = (float(xmax) - float(xmin)) / float(xbins)      

            h_tmp = TH1F('h_tmp', ' XSec Normalized #kappa_{#lambda} = ' + str(kl) , v[1], v[2], v[3])
            h_tmp.SetDirectory(0)
            h_tmp.Sumw2(1)
            for iev, event in enumerate(events):
                # print'hello'
                if iev%100 == 0: print'Event',iev 
                if iev == me: break # Max events 
                
                #event.getByLabel('prunedGenParticles', genHandle)
                events.getByLabel('genParticles', genHandle)
                genParticles = genHandle.product()
                # print'hello2'
                # Fill histograms with current variable 
                for params in pparams:
                    particle = params[0]
                    #nparticles = params[1]
                    pdgIDs = params[2]
                    ps = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in pdgIDs]                   
                    val = invmass(ps[0].p4(),ps[1].p4())
                    # h_ext.Fill(val,float(TotXSec))
                    h_tmp.Fill(val,float(TotXSec))
                    # h_ext.Fill(val,float(weight)*float(TotXSec))
                    # h_tmp.Fill(val,float(weight)*float(TotXSec))
            
            # nbins = h_tmp.GetNbinsX()
            # for ib,bv in enumerate(h_tmp): # bv = bin value 
            #     if (ib == 0): # underflow bin 
            #         continue 
            #     elif (ib == nbins + 1): # overflow bin 
            #         continue 
            #     else:
            #         xval = float(xmin + (ib - 1)*db)
            #         yval = ( float(bv) * float(weight) * float(TotXSec) ) #/ float(TotXSec)  
            #         h_tmp.Fill(xval, yval) 
                    #print'(xval,yval) = ',xval,yval 
                    #h_ext.Fill(xval, yval)
            # c2 = TCanvas('c2','c2',800,600)

            # h_tmp.SetDirectory(0)
            # h_tmp.Draw("HIST")
            h_tmp.SaveAs(ol + 'roots/sigma_normalized_k_l_' + str(kl) + '.root')

