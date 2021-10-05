#!/usr/bin/env python
# 7 February 2019
# Abe Tishelman-Charny 
# Updated 31 May 2019 for HH MC 
from ROOT import * 
import array as arr 
import numpy as np
from GEN_Plotter_Config import * 
import subprocess
#import ROOT
gROOT.SetBatch(True)
from DataFormats.FWLite import Handle, Runs, Lumis, Events  #, ChainEvent 
import sys
import os 
from os import listdir
print '.'
print 'It\'s time to plot some fun GEN variables'
print '.'
ol = '/eos/user/a/atishelm/www/HH_MC/'
# me, genHandle = -1, Handle('vector<reco::GenParticle>')
#h1 = TH1F('h1','h1',1000,0,1000)
# For each variable
for iv,v in enumerate(vs):
    print 'Plotting variable ', iv, ': ',v[0]
    # For each directory 
    for dn,d in enumerate(d):
        ch = d[0] # label1
        DID = d[1] # label2 
        direc = d[2][0] # full path of directory 
        rd = d[2][1] # direc path with root://cmsxrootd.fnal.gov/ prefix for 'Events' module  
        lc = d[3] # histo line color
        fc = d[4] # histo fill color 
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
        for ip,path in enumerate(paths):
            print '    Processing file ', ip, ': ',path 
            # kl = path.split('/')[-1].split('_')[1]
            events = Events(path) # needs to be file with root prefix 
            # h_tmp = TH1F('h_tmp', '#kappa_{#lambda} = ' + kl ,v[1],v[2],v[3])
            h_tmp = TH1F('h_tmp', 'h_tmp ',v[1],v[2],v[3])
            h_tmp.GetXaxis().SetTitle('m_{HH}')
            h_ids = TH1F('h_ids','h_ids',200,-100,100)
            # h_tmp.GetXaxis().SetRangeUser(250,1000)
            h_tmp.GetYaxis().SetTitle('Entries')
            #h_tmp.SetMinimum(-500)
            # Loop events 
            for iev, event in enumerate(events):
                if iev == me: break # Max events 
                #event.getByLabel('prunedGenParticles', genHandle)
                events.getByLabel('genParticles', genHandle)
                genParticles = genHandle.product()
                # Fill histograms with current variable 
                for params in pparams:
                    particle = params[0]
                    #nparticles = params[1]
                    pdgIDs = params[2]
                    ps = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in pdgIDs]                   
                    val = invmass(ps[0].p4(),ps[1].p4())
                    h_tmp.Fill(val)
                    
                    more_ps = [p for p in genParticles if p.isHardProcess()]
                    for mps in more_ps:
                        h_ids.Fill(mps.pdgId())
            c1 = TCanvas('c1','c1',800,600)
            h_tmp.Draw()
            h_tmp.SaveAs(ol + 'h_tmp.root')
            c1.SaveAs(ol + 'h_tmp.png')

            c2 = TCanvas('c2','c2',800,600)
            h_ids.Draw()
            h_ids.SaveAs(ol + 'h_ids.root')
            c2.SaveAs(ol + 'h_ids.png')

            print 'Finished going through events in file: ', path
            if (ip+1 == max_files): break   # Check path index 
 