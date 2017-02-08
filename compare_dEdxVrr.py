#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

c = root.TCanvas()
setupCOLZFrame(c)

#fold = root.TFile("06_15_00_v2/Likelihood_pip_v2.root")
#fnew = root.TFile("06_15_00_v2_v2/Likelihood_pip_v2.root")

fold = root.TFile("06_15_00_v2/Likelihood_p_v2.root")
fnew = root.TFile("06_15_00_v2_v2/Likelihood_p_v2.root")

treeold = fold.Get("likelihoodpidmaker/tree")
treenew = fnew.Get("likelihoodpidmaker/tree")

binningArg = [120,1.,30.,50,0.,50.]
hist2dold = Hist2D(*binningArg,TH2D=True)
hist2dnew = Hist2D(*binningArg,TH2D=True)
setHistTitles(hist2dold,"Residual Range [cm]","dE/dx [MeV/cm]")
setHistTitles(hist2dnew,"Residual Range [cm]","dE/dx [MeV/cm]")

cuts = "plane == 1"
treeold.Draw("dEdx_raw:resRange >> {0}".format(hist2dold.GetName()),cuts,"")
treenew.Draw("dEdx:resRange >> {0}".format(hist2dnew.GetName()),cuts,"")

for likelihood in [hist2dold,hist2dnew]:
  for iBinX in range(likelihood.GetNbinsX()+2):
    for iBinY in range(likelihood.GetNbinsY()+2):
      iBin = likelihood.GetBin(iBinX,iBinY)
      content = likelihood.GetBinContent(iBin)
      if content == 0:
        likelihood.SetBinContent(iBin,1e-6)
  likelihoodIntegral = likelihood.Integral()
  if likelihoodIntegral != 0.:
    likelihood.Scale(1./likelihoodIntegral)

hist2dold.Draw("colz")
c.SaveAs("Old.png")
hist2dnew.Draw("colz")
c.SaveAs("New.png")
histRatio = hist2dnew.Clone("ratio")
histRatio.Divide(hist2dold)
histRatio.Draw("colz")
c.SaveAs("Ratio.png")
histDiff = hist2dnew.Clone("diff")
histDiff.Add(hist2dold,-1.)
setNormalColorTable(True)
histDiff.Divide(hist2dold)
#histDiff.GetZaxis().SetRangeUser(-2.5e-4,2.5e-4)
histDiff.Draw("colz")
c.SaveAs("Diff.png")
