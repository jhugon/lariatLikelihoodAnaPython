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

MULTIPLYBYPITCH=False

def makeLikelihood(fileConfig,iPlane,binningArg=[325,0.,26.,200,0.,100.],evalFrac=0.1):
  ## Compute bin width from binning arg
  binWidthX = (float(binningArg[2])-binningArg[1])/binningArg[0]
  binWidthY = (float(binningArg[5])-binningArg[4])/binningArg[3]
  binCaption = "Bin size: {0:.2f} cm #times {1:.2f} MeV/cm".format(binWidthX,binWidthY)

  setupCOLZFrame(c)
  tree = fileConfig['tree']
  nEntries = tree.GetEntries()
  nSkip = int(evalFrac*nEntries)
  fileConfig['nSkip'] = nSkip
  nPlanes = fileConfig['nPlanes']
  cuts = "pdg == {0:d} && plane == {1:d}".format(fileConfig['pdg'],iPlane)
#  if fileConfig['name'] == 'p':
#    cuts += "&& true_p < 0.75"
#    cuts += "&& true_p > 0.75"
#  cuts += "&& resRange > 0.5"
  hist = Hist2D(*binningArg,TH2D=True)
  hist.SetName("pdg{0:d}_plane{1:d}".format(fileConfig['pdg'],iPlane))
  histname = hist.GetName()
  if MULTIPLYBYPITCH:
    tree.Draw("dEdx_pitchCorr:resRange >> {0}".format(histname),cuts,"",nEntries,nSkip)
  else:
    tree.Draw("dEdx_raw:resRange >> {0}".format(histname),cuts,"",nEntries,nSkip)

  setHistTitles(hist,"Residual Range [cm]","dE/dx [MeV/cm]")
  hist.Draw("colz")
  drawStandardCaptions(c,"{}, plane {}".format(fileConfig["caption"],iPlane),captionright2="Events: {0:.0f}".format(nEntries-nSkip),captionright3="Entries: {0:.0f}".format(hist.GetEntries()),captionright1=binCaption)
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
  setHistRange(likelihood,0,20,0,30)
  likelihood.Draw("colz")
  drawStandardCaptions(c,"Likelihood for {}, plane {}".format(fileConfig["title"],iPlane),captionright2="Events: {0:.0f}".format(nEntries-nSkip),captionright3="Entries: {0:.0f}".format(likelihood.GetEntries()),captionright1=binCaption,colorInside=root.kWhite)
  plotfn = "LH_{}_plane{}.png".format(fileConfig['name'],iPlane)
  c.SaveAs(plotfn)
  setupCOLZFrame(c,True)
  return hist, likelihood

def evalLogLikelihood(likelihoodHist,tree,iPlane):
  """
  Evaluates the log-likelihood for a given track
  You must have called tree.GetEntry(i) for the entry you want
  """
  result = 0.
  dEdxVec = tree.dEdx_raw
  if MULTIPLYBYPITCH:
    dEdxVec = tree.dEdx_pitchCorr
  for rr, dEdx, plane in zip(tree.resRange,dEdxVec,tree.plane):
    if iPlane == plane:
      iBin = likelihoodHist.FindBin(rr,dEdx)
      lh = likelihoodHist.GetBinContent(iBin)
      result += log(lh)
  return result

def makeLLHREffVEffGraph(likelihoodHistNum,likelihoodHistDenom,treeX,treeY,nMaxX,nMaxY,iPlane):
  valuesX = []
  for iEntry in range(nMaxX):
    treeX.GetEntry(iEntry)
    llhNum = evalLogLikelihood(likelihoodHistNum,treeX,iPlane)
    llhDenom = evalLogLikelihood(likelihoodHistDenom,treeX,iPlane)
    llhr = llhNum-llhDenom
    valuesX.append(llhr)
  valuesX.sort()
  valuesX.reverse()
  valuesY = []
  for iEntry in range(nMaxY):
    treeY.GetEntry(iEntry)
    llhNum = evalLogLikelihood(likelihoodHistNum,treeY,iPlane)
    llhDenom = evalLogLikelihood(likelihoodHistDenom,treeY,iPlane)
    llhr = llhNum-llhDenom
    valuesY.append(llhr)
  valuesY.sort()
  valuesY.reverse()
  #print min(valuesX), max(valuesX)
  #print min(valuesY), max(valuesY)
  efficiency = root.TGraph()
  for iX in range(nMaxX):
    effX = iX/float(nMaxX)
    x = valuesX[iX]
    #print x
    effY = 0.
    for iY in range(nMaxY):
      y = valuesY[iY]
      #print "    ",y
      if y <= x:
        effY = iY/float(nMaxY)
        break
    efficiency.SetPoint(iX,effX,effY)
  return efficiency

if __name__ == "__main__":

  binningArg = [520,0.,26.,400,0.,100.]
  evalFrac = 0.1
  fileConfigs = [
    {
      'fn': "06_06_01_v3/Likelihood_p_v3.root",
      'pdg': 2212,
      'name': "p",
      'title': "p",
      'caption': "proton MC sample",
      'color': root.kRed,
      'nPlanes': 2,
    },
    {
      'fn': "06_06_01_v3/Likelihood_pip_v3.root",
      'pdg': 211,
      'name': "pip",
      'title': "#pi^{+}",
      'caption': "#pi^{+} MC sample",
      'color': root.kBlue,
      'nPlanes': 2,
    },
    #{
    #  #'fn': "isoInTPC/isoInTPC_mup_v3_dEdxAllTracksNoFile.root",
    #  #'fn': "isoInTPC_v5files/isoInTPC_mup_v5_dEdxAllTracksNoFile.root",
    #  #'fn': "isoInTPC_v5filesNew/isoInTPC_mup_v5_dEdxAllTracksNoFileNew.root",
    #  'fn': "06_06_01_v2_likelihoodv2.4/likelihoodv2_mup_v2.root",
    #  'pdg': -13,
    #  'name': "mup",
    #  'title': "#mu^{+}",
    #  'caption': "#mu^{+} MC sample",
    #  'color': root.kBlack,
    #  'nPlanes': 2,
    #},
    #{
    #  #'fn': "isoInTPC/isoInTPC_kp_v3_dEdxAllTracksNoFile.root",
    #  #'fn': "isoInTPC_v5files/isoInTPC_kp_v5_dEdxAllTracksNoFile.root",
    #  #'fn': "isoInTPC_v5filesNew/isoInTPC_kp_v5_dEdxAllTracksNoFileNew.root",
    #  'fn': "06_06_01_v2_likelihoodv2.4/likelihoodv2_kp_v2.root",
    #  'pdg': 321,
    #  'name': "kp",
    #  'title': "K^{+}",
    #  'caption': "K^{+} MC sample",
    #  'color': root.kGreen+1,
    #  'nPlanes': 2,
    #},
  ]
  
  ## Compute bin width from binning arg
  binWidthX = (float(binningArg[2])-binningArg[1])/binningArg[0]
  binWidthY = (float(binningArg[5])-binningArg[4])/binningArg[3]
  
  c = root.TCanvas()
  for fileConfig in fileConfigs:
    f = root.TFile(fileConfig['fn'])
    tree = f.Get("likelihoodpidmaker/tree")
    fileConfig['f'] = f
    fileConfig['tree'] = tree
  
  outfile = root.TFile("LHPID_Templates.root","recreate")
  likelihoodsPerPlane = []
  for iPlane in range(2):
    likelihoods = {}
    for fileConfig in fileConfigs:
      #hists[fileConfig['name']], likelihoods[fileConfig['name']] = makeLikelihood(fileConfig,binningArg,evalFrac)
      hist, likelihoods[fileConfig['name']] = makeLikelihood(fileConfig,iPlane,binningArg,evalFrac)
      outfile.cd()
      hist.Write()
    likelihoodsPerPlane.append(likelihoods)
    ## Now Save Histogram File
    ## Now Evaluate
    #pipLHDiffs = [Hist(200,-1000,1000) for f in fileConfigs]
    pipLHDiffs = [Hist(100,-750,750) for f in fileConfigs]
    for fileConfig,pipLHDiff in zip(fileConfigs,pipLHDiffs):
      tree = fileConfig['tree']
      hists = []
      labels = []
      labelsRatio = []
      for fileConfig2 in fileConfigs:
        hist = Hist(100,0.,1500)
        hist.UseCurrentStyle()
        color = fileConfig2['color']
        hist.SetLineColor(color)
        hist.SetMarkerColor(color)
        hists.append(hist)
        labels.append("LH to be {}".format(fileConfig2['title']))
      assert(fileConfig['nSkip'] <= tree.GetEntries())
      for iEntry in range(fileConfig['nSkip']):
        tree.GetEntry(iEntry)
        llhpip = evalLogLikelihood(likelihoods['pip'],tree,iPlane)
        llhp = evalLogLikelihood(likelihoods['p'],tree,iPlane)
        pipLHDiff.Fill(llhpip-llhp)
        for hist, fileConfig2 in zip(hists,fileConfigs):
          llhVal = 0.
          if fileConfig2['name'] == 'pip':
            llhVal = llhpip
          elif fileConfig2['name'] == 'p':
            llhVal = llhp
          else:
            llhVal = evalLogLikelihood(likelihoods[fileConfig2['name']],tree,iPlane)
          hist.Fill(-llhVal)
      axisHist = makeStdAxisHist(hists)
      setHistTitles(axisHist,"-log(L)","Events/bin")
      axisHist.Draw()
      for hist in hists:
        showHistOverflow(hist)
        hist.Draw("histsame")
      leg = drawNormalLegend(hists,labels)
      drawStandardCaptions(c,"{}, plane {}".format(fileConfig['caption'], iPlane))
      saveName = "LHCompare_{0}_plane{1}".format(fileConfig['name'],iPlane)
      c.SaveAs(saveName+".png")
    
    # pipLLH differences
    pipLHDiffsOverflown = []
    for h, fileConfig in zip(pipLHDiffs,fileConfigs):
      h.UseCurrentStyle()
      h.SetLineColor(fileConfig['color'])
      h.Scale(1./getIntegralAll(h))
      h = h.Clone(h.GetName()+"_overflown")
      showHistOverflow(h)
      pipLHDiffsOverflown.append(h)
    axisHist = makeStdAxisHist(pipLHDiffs,freeTopSpace=0.35)
    setHistTitles(axisHist,"log(L_{#pi^{+}})-log(L_{p})","Normalized events/bin")
    #axisHist.GetXaxis().SetRangeUser(-500,500)
    axisHist.Draw()
    for h in reversed(pipLHDiffsOverflown):
      h.Draw("histsame")
    leg = drawNormalLegend(pipLHDiffs,["{} MC, {} events".format(x['title'],x['nSkip']) for x in fileConfigs])
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "LLHR_plane{0}".format(iPlane)
    c.SaveAs(saveName+".png")
    c.SaveAs(saveName+".pdf")

    # pipLLH difference integral hists

    pipLHDiffInts = []
    for h in reversed(pipLHDiffs):
      h = getIntegralHist(h)
      pipLHDiffInts.append(h)
    axisHist = makeStdAxisHist(pipLHDiffInts,freeTopSpace=0.35)
    setHistTitles(axisHist,"log(L_{#pi^{+}})-log(L_{p})","Efficiency for log(L_{#pi^{+}})-log(L_{p}) #geq X")
    axisHist.Draw()
    for h in reversed(pipLHDiffInts):
      h.Draw("histsame")
    leg = drawNormalLegend(pipLHDiffInts,["{} MC, {} events".format(x['title'],x['nSkip']) for x in fileConfigs])
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "LLHR_Effs_plane{0}".format(iPlane)
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

  ###############################################
  # Eff v Eff Curves
  pipFileConfig = [x for x in fileConfigs if x['name']=='pip'][0]
  pFileConfig = [x for x in fileConfigs if x['name']=='p'][0]
  effVeffPlane0 = makeLLHREffVEffGraph(likelihoodsPerPlane[0]['pip'],likelihoodsPerPlane[0]['p'],pipFileConfig['tree'],pFileConfig['tree'],pipFileConfig['nSkip'],pFileConfig['nSkip'],0)
  effVeffPlane1 = makeLLHREffVEffGraph(likelihoodsPerPlane[1]['pip'],likelihoodsPerPlane[1]['p'],pipFileConfig['tree'],pFileConfig['tree'],pipFileConfig['nSkip'],pFileConfig['nSkip'],1)
  axisHist = Hist2D(1,0,1.0,1,0,1.0)
  setHistTitles(axisHist,"#pi^{+} Efficiency","Proton Efficiency")
  axisHist.Draw()
  effVeffPlane0.SetLineColor(root.kRed+1)
  effVeffPlane0.SetMarkerColor(root.kRed+1)
  effVeffPlane1.SetLineColor(root.kBlue)
  effVeffPlane1.SetMarkerColor(root.kBlue)
  effVeffPlane0.SetLineWidth(3)
  effVeffPlane1.SetLineWidth(3)
  effVeffPlane1.Draw("L")
  effVeffPlane0.Draw("L")
  leg = drawNormalLegend([effVeffPlane0,effVeffPlane1],["Plane 0", "Plane 1"])
  drawStandardCaptions(c,"#pi^{+}/p likelihood ratio")
  saveName = "effVeff_pip_p"
  c.SaveAs(saveName+".png")
  c.SaveAs(saveName+".pdf")

  ########################
  outfile.Close()
