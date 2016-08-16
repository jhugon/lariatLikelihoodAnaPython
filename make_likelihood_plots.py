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

def makeLikelihoodPlot(filename,pdgid,canvas,savename,title="",dirname="dEdxAllTracks"):
  f = root.TFile(filename)
  histStr = dirname+"/TruePDG"+str(pdgid)+"plane12D"
  print filename, histStr
  hist = f.Get(histStr)

  hist.GetZaxis().SetTitle("")
  setupCOLZFrame(canvas)
  hist.UseCurrentStyle()
  #hist.SetTitle(title)
  setHistTitles(hist,"Residual Range [cm]","dE/dx [MeV/cm]")
  hist.Draw("colz")
  drawStandardCaptions(canvas,title,captionright1="Entries: {0:.0f}".format(hist.GetEntries()))
  canvas.SaveAs(savename)

canvas = root.TCanvas()
  
#makeLikelihoodPlot("05_12_01_Reco2Dnew/pip_dEdxAllTracks.root",211,canvas,"LH_beam_pip.png","Likelihood for beam-like #pi^{+}")
#makeLikelihoodPlot("05_12_01_Reco2Dnew/p_dEdxAllTracks.root",2212,canvas,"LH_beam_p.png","Likelihood for beam-like p")
#makeLikelihoodPlot("05_12_01_Reco2Dnew/kp_dEdxAllTracks.root",321,canvas,"LH_beam_kp.png","Likelihood for beam-like K^{+}")
#makeLikelihoodPlot("05_12_01_Reco2Dnew/mup_dEdxAllTracks.root",-13,canvas,"LH_beam_mup.png","Likelihood for beam-like #mu^{+}")

#makeLikelihoodPlot("isoInTPC/isoInTPC_pip_v2_dEdxAllTracks.root",211,canvas,"LH_iso_pip.png","Likelihood for isotropic, evenly-distributed #pi^{+}")
#makeLikelihoodPlot("isoInTPC/isoInTPC_p_v2_dEdxAllTracks.root",2212,canvas,"LH_iso_p.png","Likelihood for isotropic, evenly-distributed p")
#makeLikelihoodPlot("isoInTPC/isoInTPC_kp_v2_dEdxAllTracks.root",321,canvas,"LH_iso_kp.png","Likelihood for isotropic, evenly-distributed K^{+}")
#makeLikelihoodPlot("isoInTPC/isoInTPC_mup_v2_dEdxAllTracks.root",-13,canvas,"LH_iso_mup.png","Likelihood for isotropic, evenly-distributed #mu^{+}")
#makeLikelihoodPlot("isoInTPC/isoInTPC_e_v2_dEdxAllTracks.root",11,canvas,"LH_iso_e.png","Likelihood for isotropic, evenly-distributed e^{-}")

makeLikelihoodPlot("isoInTPC.bak/isoInTPC_pip_v3_dEdxAllTracks.root",211,canvas,"LH_iso_pip_v3.png","Likelihood for isotropic, evenly-distributed #pi^{+}")
makeLikelihoodPlot("isoInTPC.bak/isoInTPC_p_v3_dEdxAllTracks.root",2212,canvas,"LH_iso_p_v3.png","Likelihood for isotropic, evenly-distributed p")
makeLikelihoodPlot("isoInTPC.bak/isoInTPC_kp_v3_dEdxAllTracks.root",321,canvas,"LH_iso_kp_v3.png","Likelihood for isotropic, evenly-distributed K^{+}")
makeLikelihoodPlot("isoInTPC.bak/isoInTPC_mup_v3_dEdxAllTracks.root",-13,canvas,"LH_iso_mup_v3.png","Likelihood for isotropic, evenly-distributed #mu^{+}")
makeLikelihoodPlot("isoInTPC.bak/isoInTPC_e_v3_dEdxAllTracks.root",11,canvas,"LH_iso_e_v3.png","Likelihood for isotropic, evenly-distributed e^{-}")

makeLikelihoodPlot("isoInTPC/isoInTPC_pip_v3_dEdxAllTracksNoFile.root",211,canvas,"LH_iso_pip_v3NF.png","Likelihood for isotropic, evenly-distributed #pi^{+}",dirname="dEdxAllTracksNoFile")
makeLikelihoodPlot("isoInTPC/isoInTPC_p_v3_dEdxAllTracksNoFile.root",2212,canvas,"LH_iso_p_v3NF.png","Likelihood for isotropic, evenly-distributed p",dirname="dEdxAllTracksNoFile")
makeLikelihoodPlot("isoInTPC/isoInTPC_kp_v3_dEdxAllTracksNoFile.root",321,canvas,"LH_iso_kp_v3NF.png","Likelihood for isotropic, evenly-distributed K^{+}",dirname="dEdxAllTracksNoFile")
makeLikelihoodPlot("isoInTPC/isoInTPC_mup_v3_dEdxAllTracksNoFile.root",-13,canvas,"LH_iso_mup_v3NF.png","Likelihood for isotropic, evenly-distributed #mu^{+}",dirname="dEdxAllTracksNoFile")
makeLikelihoodPlot("isoInTPC/isoInTPC_e_v3_dEdxAllTracksNoFile.root",11,canvas,"LH_iso_e_v3NF.png","Likelihood for isotropic, evenly-distributed e^{-}",dirname="dEdxAllTracksNoFile")
