#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

"""
*Br    0 :resRange  : vector<float>                                          *
*Br    1 :pitch     : vector<float>                                          *
*Br    2 :dEdx      : vector<float>                                          *
*Br    3 :plane     : vector<unsigned int>                                   *
*Br    4 :interpE   : vector<float>                                          *
*Br    5 :interpP   : vector<float>                                          *
*Br    6 :interpDistance : vector<float>                                     *
*Br    7 :interpDistanceToClosestTrajPoint : vector<float>                   *
*Br    8 :interpIClosestTrajPoint : vector<unsigned int>                     *
*Br    9 :KE        : KE/F                                                   *
*Br   10 :nCaloHits : nCaloHits/i                                            *
*Br   11 :pdg       : pdg/I                                                  *
*Br   12 :startPosX : startPosX/F                                            *
*Br   13 :startPosY : startPosY/F                                            *
*Br   14 :startPosZ : startPosZ/F                                            *
*Br   15 :endPosX   : endPosX/F                                              *
*Br   16 :endPosY   : endPosY/F                                              *
*Br   17 :endPosZ   : endPosZ/F                                              *
*Br   18 :trkLen    : trkLen/F                                               *
*Br   19 :trkCurvyness : trkCurvyness/F                                      *
*Br   20 :matchStartDistance : matchStartDistance/F                          *
*Br   21 :matchStartAngle : matchStartAngle/F                                *
*Br   22 :matchEndDistance : matchEndDistance/F                              *
*Br   23 :matchEndAngle : matchEndAngle/F                                    *
*Br   24 :producesNTracks : producesNTracks/I                                *
*Br   25 :true_resRange : vector<float>                                      *
*Br   26 :true_dEdx : vector<float>                                          *
*Br   27 :true_trajE : vector<float>                                         *
*Br   28 :true_trajp : vector<float>                                         *
*Br   29 :true_inTPC : vector<bool>                                          *
*Br   30 :true_trajProcIs : vector<unsigned int>                             *
*Br   31 :true_trajProcNames : vector<string>                                *
*Br   32 :nTruePoints : nTruePoints/i                                        *
*Br   33 :true_ELostInTPC : true_ELostInTPC/F                                *
*Br   34 :true_E    : true_E/F                                               *
*Br   35 :true_p    : true_p/F                                               *
*Br   36 :true_thetaZenith : true_thetaZenith/F                              *
*Br   37 :true_thetaYZ : true_thetaYZ/F                                      *
*Br   38 :true_thetaYX : true_thetaYX/F                                      *
*Br   39 :true_startPosX : true_startPosX/F                                  *
*Br   40 :true_startPosY : true_startPosY/F                                  *
*Br   41 :true_startPosZ : true_startPosZ/F                                  *
*Br   42 :true_endPosX : true_endPosX/F                                      *
*Br   43 :true_endPosY : true_endPosY/F                                      *
*Br   44 :true_endPosZ : true_endPosZ/F                                      *
*Br   45 :true_length : true_length/F                                        *
*Br   46 :true_process : string                                              *
*Br   47 :true_endProcess : string                                           *
*Br   48 :true_startContained : true_startContained/O                        *
*Br   49 :true_endContained : true_endContained/O                            *

*Br   25 :pidPlane  : vector<unsigned int>                                   *
*Entries :     1915 : Total  Size=      42786 bytes  File Size  =       3428 *
*Baskets :        2 : Basket Size=      32000 bytes  Compression=  12.34     *
*............................................................................*
*Br   26 :pidChi2_p : vector<float>                                          *
*Entries :     1915 : Total  Size=      42792 bytes  File Size  =      19591 *
*Baskets :        2 : Basket Size=      32000 bytes  Compression=   2.16     *
*............................................................................*
*Br   27 :pidChi2_pi : vector<float>                                         *
*Entries :     1915 : Total  Size=      42798 bytes  File Size  =      19843 *
*Baskets :        2 : Basket Size=      32000 bytes  Compression=   2.13     *
*............................................................................*
*Br   28 :pidChi2_mu : vector<float>                                         *
*Entries :     1915 : Total  Size=      42798 bytes  File Size  =      20156 *
*Baskets :        2 : Basket Size=      32000 bytes  Compression=   2.10     *
*............................................................................*
*Br   29 :pidChi2_k : vector<float>                                          *
*Entries :     1915 : Total  Size=      42792 bytes  File Size  =      19617 *
*Baskets :        2 : Basket Size=      32000 bytes  Compression=   2.16     *
*............................................................................*
*Br   30 :PIDA      : vector<float>                                          *
*Entries :     1915 : Total  Size=      42762 bytes  File Size  =      20151 *
*Baskets :        2 : Basket Size=      32000 bytes  Compression=   2.10     *
*............................................................................*

"""

def makeLikelihood(fileConfig,iPlane,binningArg=[325,0.,26.,200,0.,100.],evalFrac=0.1):
  ## Compute bin width from binning arg
  binWidthX = (float(binningArg[2])-binningArg[1])/binningArg[0]
  binWidthY = (float(binningArg[5])-binningArg[4])/binningArg[3]
  binCaption = "Bin size: {0:.2f} mm #times {1:.2f} MeV/cm".format(binWidthX*10,binWidthY)
  nPlanes = fileConfig['nPlanes']
  nSkip = fileConfig['nSkip']
  tree = fileConfig['tree']

  setupCOLZFrame(c)
  cuts = "pdg == {0:d} && plane == {1:d}".format(fileConfig['pdg'],iPlane)
#  if fileConfig['name'] == 'p':
#    cuts += "&& true_p < 0.75"
#    cuts += "&& true_p > 0.75"
#  cuts += "&& resRange > 0.5"
  hist = Hist2D(*binningArg,TH2D=True)
  hist.SetName("pdg{0:d}_plane{1:d}".format(fileConfig['pdg'],iPlane))
  print "Making Likelihood: "+hist.GetName()
  histname = hist.GetName()
  tree.Draw("dEdx:resRange >> {0}".format(histname),cuts,"",nEntries,nSkip)

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
        likelihood.SetBinContent(iBin,1e-1)
  likelihoodIntegral = likelihood.Integral()
  if likelihoodIntegral != 0.:
    likelihood.Scale(1./likelihoodIntegral)

  setHistTitles(likelihood,"Residual Range [cm]","dE/dx [MeV/cm]")
  #setHistRange(likelihood,0,20,0,30)
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
  atLeastOneGoodHit = False
  rrNbins = likelihoodHist.GetXaxis().GetNbins()
  rrMin = likelihoodHist.GetXaxis().GetBinLowEdge(1)
  rrMax = likelihoodHist.GetXaxis().GetBinUpEdge(rrNbins)
  dEdxNbins = likelihoodHist.GetYaxis().GetNbins()
  dEdxMin = likelihoodHist.GetYaxis().GetBinLowEdge(1)
  dEdxMax = likelihoodHist.GetYaxis().GetBinUpEdge(dEdxNbins)
  for rr, dEdx, plane in zip(tree.resRange,tree.dEdx,tree.plane):
    if iPlane == plane:
      if rr > rrMin and rr < rrMax and dEdx > dEdxMin and dEdx < dEdxMax:
        iBin = likelihoodHist.FindBin(rr,dEdx)
        lh = likelihoodHist.GetBinContent(iBin)
        if lh > 1.:
          print("Warning: likelihood greater than 1: {}, for rr and dEdx: {} {}".format(lh,rr,dEdx))
        result += log(lh)
        atLeastOneGoodHit = True
  if not atLeastOneGoodHit:
    result = -1e15
  if result > 0.:
    print(result)
    print(tree.resRange)
    print(tree.dEdx)
  return result

def makeLLHREffVEffGraph(likelihoodHistNum,likelihoodHistDenom,treeX,treeY,nMaxX,nMaxY,iPlane):
  efficiency = root.TGraph()
  efficiencyPIDA = root.TGraph()
  effsX, valuesX, effsXPIDA, valuesXPIDA = findEffs(likelihoodHistNum,likelihoodHistDenom,treeX,nMaxX,iPlane)
  effsY, valuesY, effsYPIDA, valuesYPIDA = findEffs(likelihoodHistNum,likelihoodHistDenom,treeY,nMaxY,iPlane)
  nX = len(effsX)
  nY = len(effsY)
  # Eff v Eff plot
  efficiency.SetPoint(0,0,0)
  efficiencyPIDA.SetPoint(0,0,0)
  for iX in range(nX):
    effX = effsX[iX]
    effXPIDA = effsXPIDA[iX]
    x = valuesX[iX]
    xPIDA = valuesXPIDA[iX]
    #print x
    effY = 0.
    for iY in range(nY):
      y = valuesY[iY]
      #print "    ",y
      if y <= x:
        effY = effsY[iY]
        break
    efficiency.SetPoint(iX+1,effX,effY)
    effYPIDA = 0.
    #print "xPIDA: {:10.3f}".format(xPIDA)
    for iY in reversed(range(nY)):
      y = valuesYPIDA[iY]
      #print "  try yPIDA: {:10.3f}".format(y)
      if y <= xPIDA:
        effYPIDA = effsYPIDA[iY]
        break
    efficiencyPIDA.SetPoint(iX+1,effXPIDA,effYPIDA)
  efficiency.SetPoint(nX+1,1,1)
  efficiencyPIDA.SetPoint(nX+1,1,1)
  # Now print efficiency
  print("For plane: {}".format(iPlane))
  printed65 = False
  printed80 = False
  printed90 = False
  printed95 = False
  printed99 = False
  for eff, val in zip(effsX,valuesX):
    if not printed65 and eff >= 0.65:
        effYCut = None
        for effY, valY in zip(effsY,valuesY):
            if valY <= val:
                effYCut = effY
                break
        print("LH   cut value: {}, X eff: {}, Y eff: {}".format(val,eff,effYCut))
        printed65 = True
    if not printed80 and eff >= 0.8:
        effYCut = None
        for effY, valY in zip(effsY,valuesY):
            if valY <= val:
                effYCut = effY
                break
        print("LH   cut value: {}, X eff: {}, Y eff: {}".format(val,eff,effYCut))
        printed80 = True
    if not printed90 and eff >= 0.9:
        effYCut = None
        for effY, valY in zip(effsY,valuesY):
            if valY <= val:
                effYCut = effY
                break
        print("LH   cut value: {}, X eff: {}, Y eff: {}".format(val,eff,effYCut))
        printed90 = True
    if not printed95 and eff >= 0.95:
        effYCut = None
        for effY, valY in zip(effsY,valuesY):
            if valY <= val:
                effYCut = effY
                break
        print("LH   cut value: {}, X eff: {}, Y eff: {}".format(val,eff,effYCut))
        printed95 = True
    if not printed99 and eff >= 0.99:
        effYCut = None
        for effY, valY in zip(effsY,valuesY):
            if valY <= val:
                effYCut = effY
                break
        print("LH   cut value: {}, X eff: {}, Y eff: {}".format(val,eff,effYCut))
        printed99 = True
        break
  # Now print efficiency for PIDA
  printed65 = False
  printed80 = False
  printed90 = False
  printed95 = False
  printed99 = False
  for eff, val in zip(effsXPIDA,valuesXPIDA):
    if not printed65 and eff >= 0.65:
        effYCut = None
        for effY, valY in reversed(zip(effsYPIDA,valuesYPIDA)):
            if valY <= val:
                effYCut = effY
                break
        print("PIDA cut value: {}, X eff: {}, Y eff: {}".format(val,eff,effYCut))
        printed65 = True
    if not printed80 and eff >= 0.8:
        effYCut = None
        for effY, valY in reversed(zip(effsYPIDA,valuesYPIDA)):
            if valY <= val:
                effYCut = effY
                break
        print("PIDA cut value: {}, X eff: {}, Y eff: {}".format(val,eff,effYCut))
        printed80 = True
    if not printed90 and eff >= 0.9:
        effYCut = None
        for effY, valY in reversed(zip(effsYPIDA,valuesYPIDA)):
            if valY <= val:
                effYCut = effY
                break
        print("PIDA cut value: {}, X eff: {}, Y eff: {}".format(val,eff,effYCut))
        printed90 = True
    if not printed95 and eff >= 0.95:
        effYCut = None
        for effY, valY in reversed(zip(effsYPIDA,valuesYPIDA)):
            if valY <= val:
                effYCut = effY
                break
        print("PIDA cut value: {}, X eff: {}, Y eff: {}".format(val,eff,effYCut))
        printed95 = True
    if not printed99 and eff >= 0.99:
        effYCut = None
        for effY, valY in reversed(zip(effsYPIDA,valuesYPIDA)):
            if valY <= val:
                effYCut = effY
                break
        print("PIDA cut value: {}, X eff: {}, Y eff: {}".format(val,eff,effYCut))
        printed99 = True
        break
  return efficiency, efficiencyPIDA

def findEffs(likelihoodHistNum,likelihoodHistDenom,tree,nMax,iPlane):
  """
  Returns a list of efficiency values and a list of the
  corresponding cut values
  """
  values = []
  valuesPIDA = []
  n = min(nMax,tree.GetEntries())
  for iEntry in range(n):
    tree.GetEntry(iEntry)
    llhNum = evalLogLikelihood(likelihoodHistNum,tree,iPlane)
    llhDenom = evalLogLikelihood(likelihoodHistDenom,tree,iPlane)
    llhr = llhNum-llhDenom
    values.append(llhr)
    valuesPIDA.append(tree.PIDA[iPlane])
  values.sort()
  values.reverse()
  efficiency = []
  for i in range(n):
    eff = (i+1)/float(n)
    x = values[i]
    #print "LH   {:8.3f} {:8.3f}".format(x,eff)
    efficiency.append(eff)
  valuesPIDA.sort()
  #valuesPIDA.reverse()
  efficiencyPIDA = []
  print
  for i in range(n):
    eff = (i+1)/float(n)
    x = valuesPIDA[i]
    #print "PIDA {:8.3f} {:8.3f}".format(x,eff)
    efficiencyPIDA.append(eff)
  return efficiency, values, efficiencyPIDA, valuesPIDA

if __name__ == "__main__":

  binningArg = [1980,1.,100.,200,0.,50.]
  evalFrac = 0.1
  loadLikelihoodsFromFileName = None
  #loadLikelihoodsFromFileName = "LHPID_Templates_v1.root"
  fileConfigs = [
    {
      #'fn': "06_34_01_v1/new_p_v1.root",
      #'fn': "06_34_01_v2/new_p_v2.root",
      #'fn': "06_34_01_v3/new_p_v3.root",
      'fn': "06_34_01_v4/new_p_v4.root",
      'pdg': 2212,
      'name': "p",
      'title': "p",
      'caption': "proton MC sample",
      'color': root.kRed,
      'nPlanes': 2,
    },
    {
      #'fn': "06_34_01_v1/new_pip_v1.root",
      #'fn': "06_34_01_v2/new_pip_v2.root",
      #'fn': "06_34_01_v3/new_pip_v3.root",
      'fn': "06_34_01_v4/new_pip_v4.root",
      'pdg': 211,
      'name': "pip",
      'title': "#pi^{+}",
      'caption': "#pi^{+} MC sample",
      'color': root.kBlue,
      'nPlanes': 2,
    },
    #{
    #  'fn': "06_15_00_v2_v2/Likelihood_mup_v2.root",
    #  'pdg': -13,
    #  'name': "mup",
    #  'title': "#mu^{+}",
    #  'caption': "#mu^{+} MC sample",
    #  'color': root.kBlack,
    #  'nPlanes': 2,
    #},
    #{
    #  'fn': "06_15_00_v2_v2/Likelihood_kp_v2.root",
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
    #tree.Print()
    fileConfig['f'] = f
    fileConfig['tree'] = tree
    nEntries = tree.GetEntries()
    nSkip = int(evalFrac*nEntries)
    fileConfig['nSkip'] = nSkip
  
  outfile = None
  if loadLikelihoodsFromFileName:
    fileMode = "read"
    outfile = root.TFile(loadLikelihoodsFromFileName,fileMode)
  else:
    fileMode = "recreate"
    outfile = root.TFile("LHPID_Templates.root",fileMode)
  likelihoodsPerPlane = []
  for iPlane in range(2):
    likelihoods = {}
    if loadLikelihoodsFromFileName:
      for fileConfig in fileConfigs:
        histNameInFile = "pdg{0:d}_plane{1:d}".format(fileConfig['pdg'],iPlane)
        likelihood = outfile.Get(histNameInFile)
        name = likelihood.GetName() # also checking if a null pointer
        likelihood.SetName(name+"Likelihood")
        for iBinX in range(likelihood.GetNbinsX()+2):
          for iBinY in range(likelihood.GetNbinsY()+2):
            iBin = likelihood.GetBin(iBinX,iBinY)
            content = likelihood.GetBinContent(iBin)
            if content == 0:
              likelihood.SetBinContent(iBin,1e-1)
        likelihoodIntegral = likelihood.Integral()
        if likelihoodIntegral != 0.:
          likelihood.Scale(1./likelihoodIntegral)
        likelihoods[fileConfig['name']] = likelihood
    else:
      for fileConfig in fileConfigs:
        #hists[fileConfig['name']], likelihoods[fileConfig['name']] = makeLikelihood(fileConfig,binningArg,evalFrac)
        hist, likelihoods[fileConfig['name']] = makeLikelihood(fileConfig,iPlane,binningArg,evalFrac)
        outfile.cd()
        hist.Write()
    likelihoodsPerPlane.append(likelihoods)
    ## Now Save Histogram File
    ## Now Evaluate
    #pipLHDiffs = [Hist(200,-1000,1000) for f in fileConfigs]
    #pipLHDiffs = [Hist(100,-750,750) for f in fileConfigs]
    #pipLHDiffs = [Hist(50,-300,300) for f in fileConfigs]
    #PIDAHists = [Hist(50,0,50) for f in fileConfigs]
    pipLHDiffs = [Hist(100,-50,50) for f in fileConfigs]
    PIDAHists = [Hist(100,0,20) for f in fileConfigs]
    pipLHDiffStops = [Hist(50,-200,200) for f in fileConfigs]
    PIDAHistStops = [Hist(50,0,40) for f in fileConfigs]
    pipLHDiffNotStops = [Hist(50,-200,200) for f in fileConfigs]
    PIDAHistNotStops = [Hist(50,0,40) for f in fileConfigs]
    pipLHDiffVKEs = [Hist2D(100,0,1000,100,-200,200) for f in fileConfigs]
    PIDAVKEHists = [Hist2D(100,0,1000,100,0,40) for f in fileConfigs]
    for fileConfig,pipLHDiff,PIDAHist,pipLHDiffVKE,PIDAVKEHist, \
            pipLHDiffStop,PIDAHistStop,pipLHDiffNotStop,PIDAHistNotStop \
            in zip(fileConfigs,pipLHDiffs,PIDAHists,pipLHDiffVKEs,PIDAVKEHists, \
                pipLHDiffStops,PIDAHistStops,pipLHDiffNotStops,PIDAHistNotStops):
      tree = fileConfig['tree']
      hists = []
      labels = []
      labelsRatio = []
      for fileConfig2 in fileConfigs:
        hist = Hist(100,0.,3000)
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
        KE = tree.true_E - sqrt(tree.true_E**2-tree.true_p**2)
        KE *= 1000. # from GeV to MeV
        pipLHDiff.Fill(llhpip-llhp)
        pipLHDiffVKE.Fill(KE,llhpip-llhp)
        for hist, fileConfig2 in zip(hists,fileConfigs):
          llhVal = 0.
          if fileConfig2['name'] == 'pip':
            llhVal = llhpip
          elif fileConfig2['name'] == 'p':
            llhVal = llhp
          else:
            llhVal = evalLogLikelihood(likelihoods[fileConfig2['name']],tree,iPlane)
          hist.Fill(-llhVal)
        PIDAHist.Fill(tree.PIDA[iPlane])
        PIDAVKEHist.Fill(KE,tree.PIDA[iPlane])
        if tree.true_endProcess == "LArVoxelReadoutScoringProcess": # stopping
            pipLHDiffStop.Fill(llhpip-llhp)
            PIDAHistStop.Fill(tree.PIDA[iPlane])
        else:
            pipLHDiffNotStop.Fill(llhpip-llhp)
            PIDAHistNotStop.Fill(tree.PIDA[iPlane])
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

    #########################################
    ## Plot LLRs & PIDA & integrals
    #########################################
    
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
    for h in pipLHDiffs:
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

    c.SetLogy(True)
    axisHist = makeStdAxisHist(pipLHDiffInts,logy=True,ylim=[1e-5,1e2])
    setHistTitles(axisHist,"log(L_{#pi^{+}})-log(L_{p})","Efficiency for log(L_{#pi^{+}})-log(L_{p}) #geq X")
    axisHist.Draw()
    for h in reversed(pipLHDiffInts):
      h.Draw("histsame")
    leg = drawNormalLegend(pipLHDiffInts,["{} MC, {} events".format(x['title'],x['nSkip']) for x in fileConfigs])
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "LLHR_Effs_Log_plane{0}".format(iPlane)
    c.SaveAs(saveName+".png")
    c.SaveAs(saveName+".pdf")
    c.SetLogy(False)

    # PIDA
    PIDAHistsOverflown = []
    for h, fileConfig in zip(PIDAHists,fileConfigs):
      h.UseCurrentStyle()
      h.SetLineColor(fileConfig['color'])
      h.Scale(1./getIntegralAll(h))
      h = h.Clone(h.GetName()+"_overflown")
      showHistOverflow(h)
      PIDAHistsOverflown.append(h)
    axisHist = makeStdAxisHist(PIDAHists,freeTopSpace=0.35)
    setHistTitles(axisHist,"PIDA","Normalized events/bin")
    axisHist.Draw()
    for h in reversed(PIDAHistsOverflown):
      h.Draw("histsame")
    leg = drawNormalLegend(PIDAHists,["{} MC, {} events".format(x['title'],x['nSkip']) for x in fileConfigs])
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "PIDA_plane{0}".format(iPlane)
    c.SaveAs(saveName+".png")
    c.SaveAs(saveName+".pdf")

    # PIDA integral hists
    PIDAHistInts = []
    for h in PIDAHists:
      h = getIntegralHist(h,reverse=True)
      PIDAHistInts.append(h)
    axisHist = makeStdAxisHist(PIDAHistInts,freeTopSpace=0.35)
    setHistTitles(axisHist,"PIDA","Efficiency for PIDA #leq X")
    axisHist.Draw()
    for h in reversed(PIDAHistInts):
      h.Draw("histsame")
    leg = drawNormalLegend(PIDAHistInts,["{} MC, {} events".format(x['title'],x['nSkip']) for x in fileConfigs])
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "PIDA_Effs_plane{0}".format(iPlane)
    c.SaveAs(saveName+".png")
    c.SaveAs(saveName+".pdf")

    c.SetLogy(True)
    axisHist = makeStdAxisHist(PIDAHistInts,logy=True,ylim=[1e-5,1e2])
    setHistTitles(axisHist,"PIDA","Efficiency for PIDA #leq X")
    axisHist.Draw()
    for h in reversed(PIDAHistInts):
      h.Draw("histsame")
    leg = drawNormalLegend(PIDAHistInts,["{} MC, {} events".format(x['title'],x['nSkip']) for x in fileConfigs])
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "PIDA_Effs_Log_plane{0}".format(iPlane)
    c.SaveAs(saveName+".png")
    c.SaveAs(saveName+".pdf")
    c.SetLogy(False)

    ##############################################
    ###############################################
    # v KE Hists
    ##############################################
    setupCOLZFrame(c)

    # pipLLH differences v KE
    for h, fileConfig in zip(pipLHDiffVKEs,fileConfigs):
      h.UseCurrentStyle()
      setHistTitles(h,"Generated Kinetic Energy [MeV]","log(L_{#pi^{+}})-log(L_{p})")
      h.Draw("colz")
      drawStandardCaptions(c,"{} MC, {} events, plane {}".format(fileConfig['title'],fileConfig['nSkip'],iPlane))
      saveName = "LLHRVKE_{0}_plane{1}".format(fileConfig['name'],iPlane)
      c.SaveAs(saveName+".png")
      c.SaveAs(saveName+".pdf")

    # PIDA differences v KE
    for h, fileConfig in zip(PIDAVKEHists,fileConfigs):
      h.UseCurrentStyle()
      setHistTitles(h,"Generated Kinetic Energy [MeV]","PIDA")
      h.Draw("colz")
      drawStandardCaptions(c,"{} MC, {} events, plane {}".format(fileConfig['title'],fileConfig['nSkip'],iPlane))
      saveName = "PIDAVKE_{0}_plane{1}".format(fileConfig['name'],iPlane)
      c.SaveAs(saveName+".png")
      c.SaveAs(saveName+".pdf")

    setupCOLZFrame(c,True)
    ##############################################
    ###############################################
    # Stop and Not stop hists
    ##############################################

    # pipLLH differences Stop/Not
    pipLHDiffStopsOverflown = []
    for h, fileConfig in zip(pipLHDiffStops,fileConfigs):
      h.UseCurrentStyle()
      h.SetLineColor(fileConfig['color'])
      h = h.Clone(h.GetName()+"_overflown")
      showHistOverflow(h)
      pipLHDiffStopsOverflown.append(h)
    pipLHDiffNotStopsOverflown = []
    for h, fileConfig in zip(pipLHDiffNotStops,fileConfigs):
      h.UseCurrentStyle()
      h.SetLineColor(fileConfig['color'])
      h.SetLineStyle(2)
      h = h.Clone(h.GetName()+"_overflown")
      showHistOverflow(h)
      pipLHDiffNotStopsOverflown.append(h)
    axisHist = makeStdAxisHist(pipLHDiffStops+pipLHDiffNotStops,freeTopSpace=0.35)
    setHistTitles(axisHist,"log(L_{#pi^{+}})-log(L_{p})","Events/bin")
    axisHist.Draw()
    for h in reversed(pipLHDiffStopsOverflown+pipLHDiffNotStopsOverflown):
      h.Draw("histsame")
    leg = drawNormalLegend(pipLHDiffStopsOverflown+pipLHDiffNotStopsOverflown,["{} MC, Stopping".format(x['title']) for x in fileConfigs]+["{} MC, Inelastic & Decay".format(x['title']) for x in fileConfigs],wide=True)
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "LLHREndProcess_plane{0}".format(iPlane)
    c.SaveAs(saveName+".png")
    c.SaveAs(saveName+".pdf")

    # PIDA differences Stop/Not
    PIDAHistStopsOverflown = []
    for h, fileConfig in zip(PIDAHistStops,fileConfigs):
      h.UseCurrentStyle()
      h.SetLineColor(fileConfig['color'])
      h = h.Clone(h.GetName()+"_overflown")
      showHistOverflow(h)
      PIDAHistStopsOverflown.append(h)
    PIDAHistNotStopsOverflown = []
    for h, fileConfig in zip(PIDAHistNotStops,fileConfigs):
      h.UseCurrentStyle()
      h.SetLineColor(fileConfig['color'])
      h.SetLineStyle(2)
      h = h.Clone(h.GetName()+"_overflown")
      showHistOverflow(h)
      PIDAHistNotStopsOverflown.append(h)
    axisHist = makeStdAxisHist(PIDAHistStops+PIDAHistNotStops,freeTopSpace=0.35)
    setHistTitles(axisHist,"PIDA","Events/bin")
    axisHist.Draw()
    for h in reversed(PIDAHistStopsOverflown+PIDAHistNotStopsOverflown):
      h.Draw("histsame")
    leg = drawNormalLegend(PIDAHistStopsOverflown+PIDAHistNotStopsOverflown,["{} MC, Stopping".format(x['title']) for x in fileConfigs]+["{} MC, Inelastic & Decay".format(x['title']) for x in fileConfigs],wide=True)
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "PIDAEndProcess_plane{0}".format(iPlane)
    c.SaveAs(saveName+".png")
    c.SaveAs(saveName+".pdf")

    ##############################################
    ###############################################
    # Stop and Not stop efficiency (integral)
    ##############################################

    pipLHDiffStopInts = []
    pipLHDiffNotStopInts = []
    PIDAStopInts = []
    PIDANotStopInts = []
    for h in pipLHDiffStops:
        h.Scale(1./getIntegralAll(h))
        pipLHDiffStopInts.append(getIntegralHist(h))
    for h in pipLHDiffNotStops:
        h.Scale(1./getIntegralAll(h))
        pipLHDiffNotStopInts.append(getIntegralHist(h))
        h = getIntegralHist(h)
    for h in PIDAHistStops:
        h.Scale(1./getIntegralAll(h))
        PIDAStopInts.append(getIntegralHist(h,reverse=True))
    for h in PIDAHistNotStops:
        h.Scale(1./getIntegralAll(h))
        PIDANotStopInts.append(getIntegralHist(h,reverse=True))

    # pipLLR stop/not integral hists
    axisHist = makeStdAxisHist(pipLHDiffStopInts+pipLHDiffNotStopInts,freeTopSpace=0.35)
    setHistTitles(axisHist,"log(L_{#pi^{+}})-log(L_{p})","Efficiency for log(L_{#pi^{+}})-log(L_{p}) #geq X")
    axisHist.Draw()
    for h in reversed(pipLHDiffStopInts+pipLHDiffNotStopInts):
      h.Draw("histsame")
    leg = drawNormalLegend(pipLHDiffStopInts+pipLHDiffNotStopInts,["{} MC, Stopping".format(x['title']) for x in fileConfigs]+["{} MC, Inelastic & Decay".format(x['title']) for x in fileConfigs],wide=True)
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "LLHREndProcess_Effs_plane{0}".format(iPlane)
    c.SaveAs(saveName+".png")
    c.SaveAs(saveName+".pdf")

    # PIDA stop/not integral hists
    axisHist = makeStdAxisHist(PIDAStopInts+PIDANotStopInts,freeTopSpace=0.35)
    setHistTitles(axisHist,"PIDA","Efficiency for PIDA #leq X")
    axisHist.Draw()
    for h in reversed(PIDAStopInts+PIDANotStopInts):
      h.Draw("histsame")
    leg = drawNormalLegend(PIDAStopInts+PIDANotStopInts,["{} MC, Stopping".format(x['title']) for x in fileConfigs]+["{} MC, Inelastic & Decay".format(x['title']) for x in fileConfigs],wide=True)
    drawStandardCaptions(c,"Plane {}".format(iPlane))
    saveName = "PIDAEndProcess_Effs_plane{0}".format(iPlane)
    c.SaveAs(saveName+".png")
    c.SaveAs(saveName+".pdf")

  ##############################################
  ###############################################
  # Eff v Eff Curves
  ##############################################
  pipFileConfig = [x for x in fileConfigs if x['name']=='pip'][0]
  pFileConfig = [x for x in fileConfigs if x['name']=='p'][0]
#  effVeffPlane0 = makeLLHREffVEffGraph(likelihoodsPerPlane[0]['pip'],likelihoodsPerPlane[0]['p'],pipFileConfig['tree'],pFileConfig['tree'],pipFileConfig['nSkip'],pFileConfig['nSkip'],0)
  effVeffPlane1, effVeffPlane1PIDA = makeLLHREffVEffGraph(likelihoodsPerPlane[1]['pip'],likelihoodsPerPlane[1]['p'],pipFileConfig['tree'],pFileConfig['tree'],pipFileConfig['nSkip'],pFileConfig['nSkip'],1)
  axisHist = Hist2D(1,0,1.0,1,0,1.0)
  setHistTitles(axisHist,"#pi^{+} Efficiency","Proton Efficiency")
  axisHist.Draw()
#  effVeffPlane0.SetLineColor(root.kRed+1)
#  effVeffPlane0.SetMarkerColor(root.kRed+1)
#  effVeffPlane0.SetLineWidth(3)
#  effVeffPlane0.Draw("L")
  effVeffPlane1.SetLineColor(root.kBlue)
  effVeffPlane1.SetMarkerColor(root.kBlue)
  effVeffPlane1.SetLineWidth(3)
  effVeffPlane1.Draw("L")
  effVeffPlane1PIDA.SetLineColor(root.kGreen)
  effVeffPlane1PIDA.SetMarkerColor(root.kGreen)
  effVeffPlane1PIDA.SetLineWidth(3)
  effVeffPlane1PIDA.Draw("L")

  #leg = drawNormalLegend([effVeffPlane0,effVeffPlane1],["Plane 0", "Plane 1"])
  leg = drawNormalLegend([effVeffPlane1,effVeffPlane1PIDA],["Likelihood PID", "PIDA"],position=[0.2,0.7,0.6,0.89])
  drawStandardCaptions(c,"Plane 1")
  saveName = "effVeff_pip_p"
  c.SaveAs(saveName+".png")
  c.SaveAs(saveName+".pdf")

  ########################
  outfile.Close()
