#!/usr/bin/env python

# Configuration for GEN_Plotter.py 
from ROOT import * 
from DataFormats.FWLite import Handle, Runs, Lumis, Events

genHandle = Handle('vector<reco::GenParticle>')
summary = Handle('LumiSummary')
outputLoc = '/eos/user/a/atishelm/www/HH_MC'

# Particles 
ptp = []

ptp.append('H')
#ptp.append('W')
#ptp.append(all_particles["H"]) 
#ptp.append(all_particles["W"]) 
# root://cms-xrd-global.cern.ch
d = []
d.append(['/eos/cms/store/user/atishelm/HH_MC/15k/kl245/','root://cms-xrd-global.cern.ch//store/user/atishelm/HH_MC/15k/kl245/']) # end with '/'
#d.append(['label1','label2',['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X1250_WWgg_qqqqgg/withb_1000events_GEN/190613_132223/0000/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X1250_WWgg_qqqqgg/withb_1000events_GEN/190613_132223/0000/'],kMagenta,kMagenta-10])

# Variables 
# https://root.cern.ch/doc/v612/namespaceROOT_1_1Math_1_1VectorUtil.html

dphi = ROOT.Math.VectorUtil.DeltaPhi
#deltaR = ROOT.Math.VectorUtil.DeltaR
#Wphi = ROOT.Math.VectorUtil.Phi_0_2pi
invmass = ROOT.Math.VectorUtil.InvariantMass
#invmass = Math.VectorUtil.InvariantMass
# need to be methods of reco::GenParticle 
# need to do something different if it requires full vectors like angle between or invariant mass 
vs = []
#vs.append(['px',100,-1000,1000]) 
#vs.append(['py',100,-1000,1000])
#vs.append(['pz',100,-1000,1000])
# vs.append(['pt',100,0,1000])
#vs.append(['pt',100,0,1000,'ls']) #ls = plot leading and subleading. l = leading. s = subleading 
vs.append(['invm',75,250,1000]) # Invariant mass

# number of particles, files 
nps = len(ptp)
nfi = len(d)

colors=[kGreen,kGreen+2]

me = -1 # max events 
max_files= -1 # max files 

#def get_pparams(ch_,ptp_):
def get_pparams(ptp_):

    # All possible particles
    all_particles = {
    # "particle": ['<particle>',number per event,pdgID's]
    "H": ['H',2,[25]], # Higgs boson
    #"W": ['W',2,[24]], # W boson
    # "g": ['g',2,[22]], # photon
    # "q": ['q',0,[1,2,3,4,5]], # quark   # later make flavor subcategories
    # "l": ['l',0,[11,13]], # lepton
    # "nu": ['nu',0,[12,14]] # neutrino 
    }

    # # Can make subcategories of Same Flavor, Different Flavors 
    # if ch_ == 'FL':
    #     all_particles["q"][1] = 0
    #     all_particles["l"][1] = 2
    #     all_particles["nu"][1] = 2

    # elif ch_ == 'SL':
    #     all_particles["q"][1] = 2
    #     all_particles["l"][1] = 1
    #     all_particles["nu"][1] = 1

    # elif ch_ == 'FH':
    #     all_particles["q"][1] = 4
    #     all_particles["l"][1] = 0
    #     all_particles["nu"][1] = 0

    # else:
    #     print 'Cannot find particle configuration for channel: ', ch
    #     print 'Exiting'
    #     sys.exit()

    pparams_ = []
    for p_ in ptp_: 
        for key in all_particles:
            if p_ == key:
                pparams_.append(all_particles[key])

    

    return pparams_ 

# def create_h():


def order_particles(ps_):
    max_pt = 0
    nparts = len(ps_)
    tmp_ps = []
    #for i in range(len(ps_)):
        #tmp_ps.append()
        #append 
    for p in ps_:
        fourvec = ps_.p4()
        pt = fourvec.pt()
        if pt > max_pt:
            print 'not setup yet'
            
    return ops_