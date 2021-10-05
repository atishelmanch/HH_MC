#!/usr/bin/env python
# 7 February 2019
# Abe Tishelman-Charny 
# Updated 31 May 2019 for HH MC 
from ROOT import TFile, TH1F, TCanvas, gROOT, gPad, TLegend, kBlue, kGreen, gStyle, TRatioPlot
gROOT.SetBatch(True) # Don't plot on draw 
gStyle.SetOptStat(0) # no stats box 
ol = '/eos/user/a/atishelm/www/HH_MC/'
f1 = TFile('/eos/user/a/atishelm/www/HH_MC/ext_k_l_20.root')
f2 = TFile('/eos/user/a/atishelm/www/HH_MC/os_k_l_20.root')
# h_ext = f1.Get('h_ext')
# h_os = f2.Get('h_os')
# hists = []
# hists.append(h_ext)
# hists.append(h_os)
v = ['invm',75,250,1000]






# h = TH1F('h','h',10,0,10)
# h.Sumw2(1)
# h.Fill(5)
# h.Fill(5)
# h.Fill(3,3)
# h.Fill(2,2)
# c1 = TCanvas('c1','c1',800,600)
# h.Draw('hist e')
# c1.SaveAs(ol + 'testhisto2.png')

# c1 = TCanvas('c1','c1',800,600)
# h_ext.GetXaxis().SetRangeUser(250,1000)
# # h_ext.Sumw2(1)
# # h_ext.SetTitle("Extrapolated and Real #kappa_{#lambda} = 20")
# h_ext.SetLineColor(kBlue)
# h_ext.GetXaxis().SetTitle("m_{HH}")
# h_ext.GetYaxis().SetTitle("#sigma_{Total} Normalized Events")
# #h_ext.SetLineColor(6)
# h_ext.Draw("HIST e1")
# h_os.SetLineColor(kGreen)
# # h_os.SetLineWidth(6)
# h_os.SetTitle("Real #kappa_{#lambda} = 20")
# h_os.Draw("HIST same e1")
# c1.Modified()
# # h_ext.SetTitle("Extrapolated #kappa_{#lambda} = 20")
# # gPad.BuildLegend(0.75,0.75,0.95,0.95,"")
# l1 = TLegend(0.65,0.65,0.85,0.85)
# for h in hists:
#     l1.AddEntry(h,h.GetTitle(),'f')
# h_ext.SetTitle("Extrapolated and Real #kappa_{#lambda} = 20")
# l1.Draw('same') 
# c1.SaveAs(ol + 'combined_k_l_20.png')

# Get Ratio 
# xbins = v[1]
# xmin = v[2]
# xmax = v[3]
# db = (float(xmax) - float(xmin)) / float(xbins) 
# h_ratio = TH1F('ratio','(Ext / Real) - 1',xbins,v[2],v[3])
# #h_ratio.Sumw2(1)
# x_values = []
# ratios = []
# for ib,bv in enumerate(h_ext): # bv = bin value 
#     if (ib == 0): # underflow bin 
#         continue 
#     elif (ib == xbins + 1): # overflow bin 
#         continue 
#     else:
#         xval = float(xmin + (ib - 1)*db)
#         x_values.append(xval)
#         ext_value = h_ext.GetBinContent(ib)
#         real_value = h_os.GetBinContent(ib)
#         # print'ext_value = ',ext_value
#         # print'real_value = ',real_value
#         if real_value == 0:
#             continue 
#         else:
#             #ratio = float( float(ext_value) / float(real_value) )
#             ratio = float( float(ext_value) / float(real_value) ) - 1
#         ratios.append(ratio)
#         h_ratio.Fill(xval,ratio)
#         #h_ratio.Fill(xval,-1)
#         # if xval == 1000: break 
c_r = TCanvas('c_r','c_r',800,600)
h_ext_ = f1.Get('h_ext')
h_os_ = f2.Get('h_os')
hists = []
hists.append(h_ext)
hists.append(h_os)
h_ext_.Sumw2(1)
h_os_.Sumw2(1)
h_ext.SetLineColor(kBlue)
h_os.SetLineColor(kGreen)
# h_ext_.GetXaxis().SetRangeUser(250,700)
rp = TRatioPlot(h_ext_,h_os_)
rp.SetH1DrawOpt("hist e1")
c_r.SetTicks(0,1)
h_ext_.SetTitle("Extrapolated and Real #kappa_{#lambda} = 20")
rp.Draw("nogrid")
# rp.Draw()
h_ext_.GetXaxis().SetTitle('m_{HH}')
# h_ext_.GetYaxis().SetTitle('extrapolated/real')
rp.GetLowerRefGraph().GetYaxis().SetRangeUser(-1,3)
rp.GetLowerRefGraph().GetYaxis().SetTitle('Ext. / Real')
rp.GetUpperRefYaxis().SetTitle('#sigma_{total} Normalized Entries')
# rp.GetLowerRefGraph().SetTitle()
# rp.GetUpperRefGraph().SetTitle("Extrapolated and Real #kappa_{#lambda} = 20")

#rp.GetLowYaxis().SetRangeUser(-2,2)
rp.GetLowYaxis().SetNdivisions(505)
# rp.GetLowYaxis().SetMinimum(-2)
# rp.GetLowYaxis().SetMaximum(-2)
c_r.Update()
# rp.GetUpperPad().SetTitle('Extrapolated and Real #kappa_{#lambda} = 20')
width = 0.2
height = 0.2
x1 = 0.675
y1 = 0.7
# h_ext_.SetTitle("Extrapolated #kappa_{#lambda} = 20")
l1 = TLegend(x1,y1,x1+width,y1+height)
#for h in hists:
l1.AddEntry(h_ext_,"Extrapolated #kappa_{#lambda} = 20",'f')
l1.AddEntry(h_os_,"Real #kappa_{#lambda} = 20",'f')

# h_ext.SetTitle("Extrapolated and Real #kappa_{#lambda} = 20")
l1.Draw('same') 
# c_r.Modified()
c_r.SaveAs(ol + 'ratio_ext_to_real.png')

# h_ratio.GetYaxis().SetRangeUser(-1.3,1.3)
# h_ratio.GetXaxis().SetRangeUser(250,1000)
# h_ratio.GetXaxis().SetTitle("m_{HH}")
# h_ratio.SetLineColor(kBlue)
# # h_ratio.GetYaxis().SetTitle("#sigma_{Total} Normalized Events")
# c5 = TCanvas('c5','c5',800,600)
# h_ratio.Draw("HIST e1")
# c5.SaveAs(ol + 'ratio_ext_to_real.png')