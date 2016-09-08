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

true_p, true_E
"""

if __name__ == "__main__":
  c = root.TCanvas()

  fileConfigs = [
    {
      'fn': "isoInTPC_v5filesNew/isoInTPC_p_v5_dEdxAllTracksNoFileNew.root",
      'name': "pl750",
      'title': "0 < |p| < 750 MeV File",
      'caption': "0 < |p| < 750 MeV",
      'color': root.kBlue,
    },
    {
      'fn': "isoInTPC_v5filesNew/isoInTPC_to1500MeV_p_v5_dEdxAllTracksNoFile.root",
      'name': "pl1500",
      'title': "0 < |p| < 1500 MeV File",
      'caption': "0 < |p| < 1500 MeV",
      'color': root.kRed,
      'cuts': "&& true_p < 0.75"
    },
  ]
  histConfigs = [
    {
      'name': "dEdx",
      'title': "dE/dx",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized entries / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_raw",
      'cuts': "plane==1",
      'normalize': True,
      'caption': "Cutting |p| < 750 GeV",
    },
  ]

  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree",outPrefix="checkdEdx_")

  fileConfigs = [
    {
      'fn': "isoInTPC_v5filesNew/isoInTPC_to1500MeV_p_v5_dEdxAllTracksNoFile.root",
      'name': "pl1500",
    },
  ]
  histConfigs = [
    {
      'name': "dEdxVRange",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && true_p < 1.5",
      #'normalize': True,
      'caption': "0 < |p| < 1500 MeV",
    },
    {
      'name': "dEdxVRangel750",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && true_p < 0.75",
      #'normalize': True,
      'caption': "0 < |p| < 750 MeV",
    },
    {
      'name': "dEdxVRangeg750",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && true_p > 0.75 && true_p < 1.5",
      #'normalize': True,
      'caption': "750 MeV < |p| < 1500 MeV",
    },
    {
      'name': "dEdxVRangeg600l700",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && true_p > 0.60 && true_p < 0.7",
      #'normalize': True,
      'caption': "600 MeV < |p| < 700 MeV",
    },
    {
      'name': "dEdxVRangeg700l800",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && true_p > 0.70 && true_p < 0.8",
      #'normalize': True,
      'caption': "700 MeV < |p| < 800 MeV",
    },
    {
      'name': "dEdxVRangeg800l900",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && true_p > 0.80 && true_p < 0.9",
      #'normalize': True,
      'caption': "800 MeV < |p| < 900 MeV",
    },
    {
      'name': "dEdxVmom",
      'xtitle': "Proton true momentum [MeV/c]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [40,300.,1500.,30,0.,30.],
      'var': "dEdx_raw:true_p*1000.",
      'cuts': "plane==1 && resRange > 5. && resRange < 10.",
      #'normalize': True,
      'caption': "5 cm < residual range < 10 cm",
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree",outPrefix="checkpmom_")

