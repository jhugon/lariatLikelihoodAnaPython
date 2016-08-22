#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

from rootpy.plotting import Hist, Hist2D, Canvas, Graph

"""
*Br    0 :resRange  : vector<float>                                          *
*Br    1 :pitchCorr : vector<float>                                          *
*Br    2 :dEdx_raw  : vector<float>                                          *
*Br    3 :dEdx_pitchCorr : vector<float>                                     *
*Br    4 :plane     : vector<unsigned int>                                   *
*Br    5 :KE        : KE/F                                                   *
*Br    6 :nCaloHits : nCaloHits/i                                            *
*Br    7 :pdg       : pdg/I                                                  *
"""

def makeLikelihood(fileConfig,binningArg=[325,0.,26.,200,0.,100.],evalFrac=0.1):
  setupCOLZFrame(c)
  tree = fileConfig['tree']
  nEntries = tree.GetEntries()
  nSkip = int(evalFrac*nEntries)
  fileConfig['nSkip'] = nSkip
  cuts = "pdg == {0:d}".format(fileConfig['pdg'])
  hist = Hist2D(*binningArg)
  histname = hist.GetName()
  tree.Draw("dEdx_pitchCorr:resRange >> {0}".format(histname),cuts,"",nEntries,nSkip)

  setHistTitles(hist,"Residual Range [cm]","dE/dx [MeV/cm]")
  setHistRange(hist,0,10,0,20)
  hist.Draw("colz")
  drawStandardCaptions(c,"Likelihood for {}".format(fileConfig["title"]),captionright1="Entries: {0:.0f}".format(hist.GetEntries()))
  plotfn = "dEdxVrange_{}.png".format(fileConfig['name'])
  c.SaveAs(plotfn)

  for iBinX in range(hist.GetNbinsX()+2):
    for iBinY in range(hist.GetNbinsY()+2):
      iBin = hist.GetBin(iBinX,iBinY)
      content = hist.GetBinContent(iBin)
      if content == 0:
        hist.SetBinContent(iBin,0.001)
  histIntegral = hist.Integral()
  if histIntegral != 0.:
    hist.Scale(1./histIntegral)


  setHistTitles(hist,"Residual Range [cm]","dE/dx [MeV/cm]")
  hist.Draw("colz")
  drawStandardCaptions(c,"Likelihood for {}".format(fileConfig["title"]),captionright1="Entries: {0:.0f}".format(hist.GetEntries()))
  plotfn = "LH_{}.png".format(fileConfig['name'])
  c.SaveAs(plotfn)
  setupCOLZFrame(c,True)
  return hist

def evalLogLikelihood(likelihoodHist,tree):
  """
  Evaluates the log-likelihood for a given track
  You must have called tree.GetEntry(i) for the entry you want
  """
  result = 0.
  for rr, dEdx in zip(tree.resRange,tree.dEdx_pitchCorr):
    iBin = likelihoodHist.FindBin(rr,dEdx)
    lh = likelihoodHist.GetBinContent(iBin)
    result += log(lh)
  return result

if __name__ == "__main__":

  binningArg = [325,0.,26.,200,0.,100.]
  evalFrac = 0.1
  fileConfigs = [
    {
      'fn': "isoInTPC/isoInTPC_mup_v3_dEdxAllTracksNoFile.root",
      'pdg': -13,
      'name': "mup",
      'title': "#mu^{+}",
      'color': root.kRed,
    },
    {
      'fn': "isoInTPC/isoInTPC_pip_v3_dEdxAllTracksNoFile.root",
      'pdg': 211,
      'name': "pip",
      'title': "#pi^{+}",
      'color': root.kBlack,
    },
    {
      'fn': "isoInTPC/isoInTPC_p_v3_dEdxAllTracksNoFile.root",
      'pdg': 2212,
      'name': "p",
      'title': "p",
      'color': root.kGreen+1,
    },
    {
      'fn': "isoInTPC/isoInTPC_kp_v3_dEdxAllTracksNoFile.root",
      'pdg': 321,
      'name': "kp",
      'title': "K^{+}",
      'color': root.kBlue,
    },
  ]
  
  
  c = root.TCanvas()
  for fileConfig in fileConfigs:
    f = root.TFile(fileConfig['fn'])
    tree = f.Get("dEdxAllTracksNoFile/tree")
    fileConfig['f'] = f
    fileConfig['tree'] = tree
  
  likelihoods = {}
  for fileConfig in fileConfigs:
    likelihoods[fileConfig['name']] = makeLikelihood(fileConfig,binningArg,evalFrac)
  pipLHRs = [Hist(100,0,2) for f in fileConfigs]
  for fileConfig,pipLHR in zip(fileConfigs,pipLHRs):
    tree = fileConfig['tree']
    hists = []
    labels = []
    histsRatio = []
    labelsRatio = []
    for fileConfig2 in fileConfigs:
      hist = Hist(20,0,400)
      hist.UseCurrentStyle()
      color = fileConfig2['color']
      hist.SetLineColor(color)
      hist.SetMarkerColor(color)
      hists.append(hist)
      labels.append("LH to be {}".format(fileConfig2['title']))
      if fileConfig2['name'] != fileConfig['name']:
        hist = Hist(100,0,2)
        hist.UseCurrentStyle()
        color = fileConfig2['color']
        hist.SetLineColor(color)
        hist.SetMarkerColor(color)
        histsRatio.append(hist)
        labelsRatio.append("LH Ratio {0}/{1}".format(fileConfig['title'],fileConfig2['title']))
      else:
        histsRatio.append(None)
    assert(fileConfig['nSkip'] <= tree.GetEntries())
    for iEntry in range(fileConfig['nSkip']):
      tree.GetEntry(iEntry)
      #numeratorLH = evalLogLikelihood(likelihoods[fileConfig['name']],tree)
      #for hist, histRatio, fileConfig2 in zip(hists,histsRatio,fileConfigs):
      #  likelihood = likelihoods[fileConfig2['name']]
      #  likelihoodTitle = fileConfig2['title']
      #  logLikelihoodVal = evalLogLikelihood(likelihood,tree)
      #  hist.Fill(-logLikelihoodVal)
      #  if histRatio:
      #    if logLikelihoodVal == 0.:
      #      hist.Fill(1e15)
      #    else:
      #      histRatio.Fill(numeratorLH/logLikelihoodVal)
      llhpip = evalLogLikelihood(likelihoods['pip'],tree)
      llhp = evalLogLikelihood(likelihoods['p'],tree)
      if llhp == 0.:
        pipLHR.Fill(1e15)
      else:
        pipLHR.Fill(llhpip/llhp)
    axisHist = makeStdAxisHist(hists)
    setHistTitles(axisHist,"-log(L)","Events/bin")
    axisHist.Draw()
    for hist in hists:
      hist.Draw("histsame")
    leg = drawNormalLegend(hists,labels)
    drawStandardCaptions(c,"{} MC Sample".format(fileConfig['title']))
    saveName = "LHCompare_{0}".format(fileConfig['name'])
    c.SaveAs(saveName+".png")
  
    histsRatio = [x for x in histsRatio if x]
    axisHist = makeStdAxisHist(histsRatio)
    setHistTitles(axisHist,"log(L_{{{0}}})/Log(L_{{X}})".format(fileConfig['title']),"Events/bin")
    axisHist.Draw()
    for hist in histsRatio:
      hist.Draw("histsame")
    leg = drawNormalLegend(histsRatio,labelsRatio)
    drawStandardCaptions(c,"{} MC Sample".format(fileConfig['title']))
    saveName = "LHRatioCompare_{0}".format(fileConfig['name'])
    c.SaveAs(saveName+".png")

  # pipLHRs
  for h, fileConfig in zip(pipLHRs,fileConfigs):
    h.UseCurrentStyle()
    h.SetLineColor(fileConfig['color'])
  axisHist = makeStdAxisHist(pipLHRs)
  setHistTitles(axisHist,"log(L_{#pi^{+}})/log(L_{p})","Events/bin")
  axisHist.Draw()
  for h in pipLHRs:
    h.Draw("histsame")
  leg = drawNormalLegend(pipLHRs,["{} MC".format(x['title']) for x in fileConfigs])
  c.SaveAs("LLHR.png")
