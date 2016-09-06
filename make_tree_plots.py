#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

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

def makeLikelihood(fileConfig,iPlane,binningArg=[325,0.,26.,200,0.,100.],evalFrac=0.1):
  setupCOLZFrame(c)
  tree = fileConfig['tree']
  nEntries = tree.GetEntries()
  nSkip = int(evalFrac*nEntries)
  fileConfig['nSkip'] = nSkip
  nPlanes = fileConfig['nPlanes']
  cuts = "pdg == {0:d} && plane == {1:d}".format(fileConfig['pdg'],iPlane)
  hist = Hist2D(*binningArg,TH2D=True)
  hist.SetName("pdg{0:d}_plane{1:d}".format(fileConfig['pdg'],iPlane))
  histname = hist.GetName()
  tree.Draw("dEdx_pitchCorr:resRange >> {0}".format(histname),cuts,"",nEntries,nSkip)

  setHistTitles(hist,"Residual Range [cm]","dE/dx [MeV/cm]")
  hist.Draw("colz")
  drawStandardCaptions(c,"{}, plane {}".format(fileConfig["caption"],iPlane),captionright1="Events: {0:.0f}".format(nEntries-nSkip),captionright2="Entries: {0:.0f}".format(hist.GetEntries()))
  plotfn = "dEdxVrange_{}_plane{}.png".format(fileConfig['name'],iPlane)
  c.SaveAs(plotfn)

  likelihood = hist.Clone(hist.GetName()+"Likelihood")

  for iBinX in range(likelihood.GetNbinsX()+2):
    for iBinY in range(likelihood.GetNbinsY()+2):
      iBin = likelihood.GetBin(iBinX,iBinY)
      content = likelihood.GetBinContent(iBin)
      if content == 0:
        likelihood.SetBinContent(iBin,0.001)
  likelihoodIntegral = likelihood.Integral()
  if likelihoodIntegral != 0.:
    likelihood.Scale(1./likelihoodIntegral)

  setHistTitles(likelihood,"Residual Range [cm]","dE/dx [MeV/cm]")
  setHistRange(likelihood,0,10,0,20)
  likelihood.Draw("colz")
  drawStandardCaptions(c,"Likelihood for {}, plane {}".format(fileConfig["title"],iPlane),captionright1="Events: {0:.0f}".format(nEntries-nSkip),captionright2="Entries: {0:.0f}".format(likelihood.GetEntries()))
  plotfn = "LH_{}_plane{}.png".format(fileConfig['name'],iPlane)
  c.SaveAs(plotfn)
  setupCOLZFrame(c,True)
  return hist, likelihood

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
      #'fn': "isoInTPC_v5files/isoInTPC_p_v5_dEdxAllTracksNoFile.root",
      'fn': "isoInTPC_v5filesNew/isoInTPC_p_v5_dEdxAllTracksNoFileNew.root",
      'pdg': 2212,
      'name': "p",
      'title': "p",
      'caption': "proton MC sample",
      'color': root.kGreen+1,
      'nPlanes': 2,
    },
    {
      #'fn': "isoInTPC_v5files/isoInTPC_pip_v5_dEdxAllTracksNoFile.root",
      'fn': "isoInTPC_v5filesNew/isoInTPC_pip_v5_dEdxAllTracksNoFileNew.root",
      'pdg': 211,
      'name': "pip",
      'title': "#pi^{+}",
      'caption': "#pi^{+} MC sample",
      'color': root.kBlack,
      'nPlanes': 2,
    },
    {
      #'fn': "isoInTPC_v5files/isoInTPC_mup_v5_dEdxAllTracksNoFile.root",
      'fn': "isoInTPC_v5filesNew/isoInTPC_mup_v5_dEdxAllTracksNoFileNew.root",
      'pdg': -13,
      'name': "mup",
      'title': "#mu^{+}",
      'caption': "#mu^{+} MC sample",
      'color': root.kRed,
      'nPlanes': 2,
    },
    {
      #'fn': "isoInTPC_v5files/isoInTPC_kp_v5_dEdxAllTracksNoFile.root",
      'fn': "isoInTPC_v5filesNew/isoInTPC_kp_v5_dEdxAllTracksNoFileNew.root",
      'pdg': 321,
      'name': "kp",
      'title': "K^{+}",
      'caption': "K^{+} MC sample",
      'color': root.kBlue,
      'nPlanes': 2,
    },
  ]
  
  
  c = root.TCanvas()
  for fileConfig in fileConfigs:
    f = root.TFile(fileConfig['fn'])
    tree = f.Get("dEdxAllTracksNoFile/tree")
    fileConfig['f'] = f
    fileConfig['tree'] = tree
  
  outfile = root.TFile("LHPID_Templates.root","recreate")
  for iPlane in range(2):
    likelihoods = {}
    for fileConfig in fileConfigs:
      #hists[fileConfig['name']], likelihoods[fileConfig['name']] = makeLikelihood(fileConfig,binningArg,evalFrac)
      hist, likelihoods[fileConfig['name']] = makeLikelihood(fileConfig,iPlane,binningArg,evalFrac)
      outfile.cd()
      hist.Write()
    ## Now Save Histogram File
    ## Now Evaluate
    pipLHDiffs = [Hist(100,-200,200) for f in fileConfigs]
    for fileConfig,pipLHDiff in zip(fileConfigs,pipLHDiffs):
      tree = fileConfig['tree']
      hists = []
      labels = []
      labelsRatio = []
      for fileConfig2 in fileConfigs:
        hist = Hist(100,0.,5000)
        hist.UseCurrentStyle()
        color = fileConfig2['color']
        hist.SetLineColor(color)
        hist.SetMarkerColor(color)
        hists.append(hist)
        labels.append("LH to be {}".format(fileConfig2['title']))
      assert(fileConfig['nSkip'] <= tree.GetEntries())
      for iEntry in range(fileConfig['nSkip']):
        tree.GetEntry(iEntry)
        llhpip = evalLogLikelihood(likelihoods['pip'],tree)
        llhp = evalLogLikelihood(likelihoods['p'],tree)
        pipLHDiff.Fill(llhpip-llhp)
        for hist, fileConfig2 in zip(hists,fileConfigs):
          llhVal = 0.
          if fileConfig2['name'] == 'pip':
            llhVal = llhpip
          elif fileConfig2['name'] == 'p':
            llhVal = llhp
          else:
            llhVal = evalLogLikelihood(likelihoods[fileConfig2['name']],tree)
          hist.Fill(-llhVal)
      axisHist = makeStdAxisHist(hists)
      setHistTitles(axisHist,"-log(L)","Events/bin")
      axisHist.Draw()
      for hist in hists:
        hist.Draw("histsame")
      leg = drawNormalLegend(hists,labels)
      drawStandardCaptions(c,"{}, plane {}".format(fileConfig['caption'], iPlane))
      saveName = "LHCompare_{0}_plane{1}".format(fileConfig['name'],iPlane)
      c.SaveAs(saveName+".png")
    
    # pipLLH differences
    for h, fileConfig in zip(pipLHDiffs,fileConfigs):
      h.UseCurrentStyle()
      h.SetLineColor(fileConfig['color'])
    axisHist = makeStdAxisHist(pipLHDiffs,freeTopSpace=0.35)
    setHistTitles(axisHist,"log(L_{#pi^{+}})-log(L_{p})","Events/bin")
    axisHist.Draw()
    for h in reversed(pipLHDiffs):
      h.Draw("histsame")
    leg = drawNormalLegend(pipLHDiffs,["{} MC, {} events".format(x['title'],x['nSkip']) for x in fileConfigs])
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "LLHR_plane{0}".format(iPlane)
    c.SaveAs(saveName+".png")
    c.SaveAs(saveName+".pdf")

    ###############################################3
    ## Investigate track pitch
    #histConfigs = [
    #  {
    #    'name': "pitch_plane{0}".format(iPlane),
    #    'xtitle': "Pitch [cm]",
    #    'ytitle': "Entries/bin",
    #    #'binning': [100,0,25],
    #    'binning': getLogBins(100,0.4,1e4),
    #    'var': "pitchCorr",
    #    'cuts': "",
    #    'logx': True,
    #    'logy': True,
    #  },
    #]
    #plotOneHistOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree")
  outfile.Close()
