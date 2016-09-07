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

if __name__ == "__main__":
  c = root.TCanvas()

  fileConfigs = [
    {
      'fn': "isoInTPC_v5filesNew/isoInTPC_mup_v5_dEdxAllTracksNoFileNew.root",
      'pdg': -13,
      'name': "mup",
      'title': "#mu^{+}",
      'caption': "#mu^{+} MC sample",
      'captionleft1': "Plane 1",
      'color': root.kRed,
      'nPlanes': 2,
      
    },
  ]
  histConfigs = [
    {
      'name': "dEdx_raw",
      'title': "dE/dx Raw",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_raw",
      'cuts': "plane==1 && resRange > 1.",
      'color': root.kBlack,
      'normalize': True,
    },
    {
      'name': "dEdx_raw",
      'title': "dE/dx Raw, pitch > 1 cm",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_raw",
      'cuts': "plane==1 && resRange > 1. && pitchCorr > 1.",
      'color': root.kGreen+1,
      'normalize': True,
    },
    {
      'name': "dEdx_raw",
      'title': "dE/dx Raw, pitch > 1.5 cm",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_raw",
      'cuts': "plane==1 && resRange > 1. && pitchCorr > 1.5",
      'color': root.kBlue,
      'normalize': True,
    },
    {
      'name': "dEdx_pitchCorr",
      'title': "dE/dx * pitch",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_pitchCorr",
      'cuts': "plane==1 && resRange > 1.",
      'color': root.kRed,
      'normalize': True,
    },
    {
      'name': "dEdx_pitchCorr",
      'title': "dE/dx * pitch, pitch > 1 cm",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_pitchCorr",
      'cuts': "plane==1 && resRange > 1. && pitchCorr > 1.",
      'color': root.kCyan,
      'normalize': True,
    },
    {
      'name': "dEdx_pitchCorr",
      'title': "dE/dx * pitch, pitch > 1.5 cm",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_pitchCorr",
      'cuts': "plane==1 && resRange > 1. && pitchCorr > 1.5",
      'color': root.kMagenta,
      'normalize': True,
    },
  ]

  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree",outPrefix="pitchdEdxPlane1")

  fileConfigs = [
    {
      'fn': "isoInTPC_v5filesNew/isoInTPC_mup_v5_dEdxAllTracksNoFileNew.root",
      'pdg': -13,
      'name': "mup",
      'title': "#mu^{+}",
      'caption': "#mu^{+} MC sample",
      'captionleft1': "Plane 0",
      'color': root.kRed,
      'nPlanes': 2,
      
    },
  ]
  histConfigs = [
    {
      'name': "dEdx_raw",
      'title': "dE/dx Raw",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_raw",
      'cuts': "plane==0 && resRange > 1.",
      'color': root.kBlack,
      'normalize': True,
    },
    {
      'name': "dEdx_raw",
      'title': "dE/dx Raw, pitch > 1 cm",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_raw",
      'cuts': "plane==0 && resRange > 1. && pitchCorr > 1.",
      'color': root.kGreen+1,
      'normalize': True,
    },
    {
      'name': "dEdx_raw",
      'title': "dE/dx Raw, pitch > 1.5 cm",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_raw",
      'cuts': "plane==0 && resRange > 1. && pitchCorr > 1.5",
      'color': root.kBlue,
      'normalize': True,
    },
    {
      'name': "dEdx_pitchCorr",
      'title': "dE/dx * pitch",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_pitchCorr",
      'cuts': "plane==0 && resRange > 1.",
      'color': root.kRed,
      'normalize': True,
    },
    {
      'name': "dEdx_pitchCorr",
      'title': "dE/dx * pitch, pitch > 1 cm",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_pitchCorr",
      'cuts': "plane==0 && resRange > 1. && pitchCorr > 1.",
      'color': root.kCyan,
      'normalize': True,
    },
    {
      'name': "dEdx_pitchCorr",
      'title': "dE/dx * pitch, pitch > 1.5 cm",
      'xtitle': "dE/dx [MeV/cm]",
      'ytitle': "Normalized Events / bin",
      'binning': [100,0.0,20],
      'var': "dEdx_pitchCorr",
      'cuts': "plane==0 && resRange > 1. && pitchCorr > 1.5",
      'color': root.kMagenta,
      'normalize': True,
    },
  ]

  c = root.TCanvas()
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree",outPrefix="pitchdEdxPlane0")


  histConfigs = [
    {
      'name': "pitch",
      'title': "Plane 0",
      'xtitle': "pitch [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0.0,20],
      'var': "pitchCorr",
      'cuts': "plane==0",
      'color': root.kRed,
    },
    {
      'name': "pitch",
      'title': "Plane 1",
      'xtitle': "pitch [cm]",
      'ytitle': "Events / bin",
      'binning': [100,0.0,20],
      'var': "pitchCorr",
      'cuts': "plane==1",
    },
  ]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree",outPrefix="pitch")
