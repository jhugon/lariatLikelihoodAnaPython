#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

def drawNormalLegend(hists,labels,option="l"):
  assert(len(hists)==len(labels))
  #leg = root.TLegend(0.55,0.6,0.91,0.89)
  leg = root.TLegend(0.35,0.6,0.91,0.89)
  leg.SetLineColor(root.kWhite)
  for hist,label in zip(hists,labels):
    leg.AddEntry(hist,label,option)
  return leg

def setupCOLZFrame(pad,reset=False):
  if reset:
    pad.SetRightMargin(gStyle.GetPadRightMargin())
  else:
    pad.SetRightMargin(0.15)

c = root.TCanvas()

fold = root.TFile("05_01_00/mu_dEdxAllTracks.root")
fnew = root.TFile("05_12_01_Reco2Dnew/mup_dEdxAllTracks.root")

hist2dold = fold.Get("dEdxAllTracks/TruePDG-13plane12D")
hist2dnew = fnew.Get("dEdxAllTracks/TruePDG-13plane12D")

hist1dold = fold.Get("dEdxAllTracks/TruePDG-13plane1")
hist1dnew = fnew.Get("dEdxAllTracks/TruePDG-13plane1")

hist1dold.UseCurrentStyle()
hist1dnew.UseCurrentStyle()
hist1dold.SetLineColor(root.kGreen+2)
hist1dnew.SetLineColor(root.kBlue+2)
#setHistTitles(hist1dold,"dE/dx [MeV/cm]","Counts")
normalizeHist(hist1dold)
normalizeHist(hist1dnew)
setHistTitles(hist1dold,"dE/dx [MeV/cm]","Arbitrary units")

leg = drawNormalLegend([hist1dold,hist1dnew],["Andrew's 5_01_00", "Justin's 5_12_01 RecoMC.fcl"])

hist1dold.Draw("")
hist1dnew.Draw("same")

leg.Draw()

c.SaveAs("dEdx.png")
c.SaveAs("dEdx.pdf")

###################################################################
hist2dold.GetZaxis().SetTitle("")
hist2dnew.GetZaxis().SetTitle("")
setupCOLZFrame(c)

hist2dold.UseCurrentStyle()
hist2dold.SetTitle("Andrew's 5_01_00")
setHistTitles(hist2dold,"Residual Range [cm]","dE/dx [MeV/cm]")
hist2dold.Draw("colz")

c.SaveAs("dEdxVl_05_01_00.png")
#c.SaveAs("dEdxVl_05_01_00.pdf")

hist2dnew.UseCurrentStyle()
hist2dnew.SetTitle("Justin's 5_12_01")
setHistTitles(hist2dnew,"Residual Range [cm]","dE/dx [MeV/cm]")
hist2dnew.Draw("colz")

c.SaveAs("dEdxVl_05_12_01.png")
#c.SaveAs("dEdxVl_05_12_01.pdf")

######################################################################

setupCOLZFrame(c,True)
c.Clear()

fold = root.TFile("05_01_00/dEdxAnalysis.root")
fnew = root.TFile("05_12_01/dEdxAnalysis.root")

histHitUold = fold.Get("dEdxAnalyzer/dQdxU")
histHitUnew = fnew.Get("dEdxAnalyzer/dQdxU")

histHitVold = fold.Get("dEdxAnalyzer/dQdxV")
histHitVnew = fnew.Get("dEdxAnalyzer/dQdxV")

histdEdxCaloold = fold.Get("dEdxAnalyzer/dEdxCalo")
histdEdxCalonew = fnew.Get("dEdxAnalyzer/dEdxCalo")

histhitPeakAmplitudeold = fold.Get("dEdxAnalyzer/hitPeakAmplitude")
histhitPeakAmplitudenew = fnew.Get("dEdxAnalyzer/hitPeakAmplitude")

histhitIntegralold = fold.Get("dEdxAnalyzer/hitIntegral")
histhitIntegralnew = fnew.Get("dEdxAnalyzer/hitIntegral")

histHitUold.UseCurrentStyle()
histHitVold.UseCurrentStyle()
histHitUnew.UseCurrentStyle()
histHitVnew.UseCurrentStyle()
histdEdxCaloold.UseCurrentStyle()
histdEdxCalonew.UseCurrentStyle()
histHitUold.SetLineColor(root.kGreen+2)
histHitUnew.SetLineColor(root.kBlue+2)
histHitVold.SetLineColor(root.kGreen+2)
histHitVnew.SetLineColor(root.kBlue+2)
histdEdxCaloold.SetLineColor(root.kGreen+2)
histdEdxCalonew.SetLineColor(root.kBlue+2)
histhitPeakAmplitudeold.SetLineColor(root.kGreen+2)
histhitPeakAmplitudenew.SetLineColor(root.kBlue+2)
histhitIntegralold.SetLineColor(root.kGreen+2)
histhitIntegralnew.SetLineColor(root.kBlue+2)

histHitUold.GetXaxis().SetRangeUser(100,10000)
setHistTitles(histHitUold,"dQ/dx for U Plane [??]","Counts")
histHitUold.Draw()
histHitUnew.Draw("same")
leg = drawNormalLegend([histHitUold,histHitUnew],["Andrew's 5_01_00", "Justin's 5_12_01"])
leg.Draw()
c.SaveAs("dQdxU.png")

histHitVold.GetXaxis().SetRangeUser(100,10000)
setHistTitles(histHitVold,"dQ/dx for V Plane [??]","Counts")
histHitVold.Draw()
histHitVnew.Draw("same")
leg = drawNormalLegend([histHitVold,histHitVnew],["Andrew's 5_01_00", "Justin's 5_12_01"])
leg.Draw()
c.SaveAs("dQdxV.png")

histdEdxCaloold.GetXaxis().SetRangeUser(0,100)
setHistTitles(histdEdxCaloold,"dE/dx from Calo Objects [??]","Counts")
histdEdxCaloold.Draw()
histdEdxCalonew.Draw("same")
leg = drawNormalLegend([histdEdxCaloold,histdEdxCalonew],["Andrew's 5_01_00", "Justin's 5_12_01"])
leg.Draw()
c.SaveAs("dEdxCalo.png")

histhitPeakAmplitudeold.GetXaxis().SetRangeUser(0,200)
setHistTitles(histhitPeakAmplitudeold,"Hit Peak Amplitude [??]","Counts")
histhitPeakAmplitudeold.Draw()
histhitPeakAmplitudenew.Draw("same")
leg = drawNormalLegend([histhitPeakAmplitudeold,histhitPeakAmplitudenew],["Andrew's 5_01_00", "Justin's 5_12_01"])
leg.Draw()
c.SaveAs("hitPeakAmplitude.png")

histhitIntegralold.GetXaxis().SetRangeUser(0,4000)
setHistTitles(histhitIntegralold,"Hit Integral [??]","Counts")
histhitIntegralold.Draw()
histhitIntegralnew.Draw("same")
leg = drawNormalLegend([histhitIntegralold,histhitIntegralnew],["Andrew's 5_01_00", "Justin's 5_12_01"])
leg.Draw()
c.SaveAs("hitIntegral.png")

