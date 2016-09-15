#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

"""
*Br    0 :resRange  : vector<float>
*Br    1 :pitchCorr : vector<float>
*Br    2 :dEdx_raw  : vector<float>
*Br    3 :dEdx_pitchCorr : vector<float>
*Br    4 :plane     : vector<unsigned int>
*Br    5 :KE        : KE/F
*Br    6 :nCaloHits : nCaloHits/i
*Br    7 :pdg       : pdg/I
*Br    8 :startPosX : startPosX/F
*Br    9 :startPosY : startPosY/F
*Br   10 :startPosZ : startPosZ/F
*Br   11 :endPosX   : endPosX/F
*Br   12 :endPosY   : endPosY/F
*Br   13 :endPosZ   : endPosZ/F
*Br   14 :true_resRange : vector<float>
*Br   15 :true_dEdx : vector<float>
*Br   16 :true_inTPC : vector<bool>
*Br   17 :nTruePoints : nTruePoints/i
*Br   18 :true_ELostInTPC : true_ELostInTPC/F
*Br   19 :true_E    : true_E/F
*Br   20 :true_p    : true_p/F
*Br   21 :true_thetaZenith : true_thetaZenith/F
*Br   22 :true_thetaYZ : true_thetaYZ/F
*Br   23 :true_thetaYX : true_thetaYX/F
*Br   24 :true_startPosX : true_startPosX/F
*Br   25 :true_startPosY : true_startPosY/F
*Br   26 :true_startPosZ : true_startPosZ/F
*Br   27 :true_endPosX : true_endPosX/F
*Br   28 :true_endPosY : true_endPosY/F
*Br   29 :true_endPosZ : true_endPosZ/F
*Br   30 :true_process : string
*Br   31 :true_endProcess : string
"""

if __name__ == "__main__":
  c = root.TCanvas()

  fileConfigs = [
    {
      #'fn': "isoInTPC_v5filesNew/isoInTPC_p_v5_dEdxAllTracksNoFileNew.root",
      'fn': "isoInTPC_v5filesNewNew/dEdxAllTracksNoFile_p_v5.root",
      'name': "pl750",
      'title': "0 < |p| < 750 MeV File",
      'caption': "0 < |p| < 750 MeV",
      'color': root.kBlue,
    },
    {
      #'fn': "isoInTPC_v5filesNew/isoInTPC_to1500MeV_p_v5_dEdxAllTracksNoFile.root",
      'fn': "isoInTPC_v5filesNewNew/dEdxAllTracksNoFile_to1500MeV_p_v5.root",
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
      #'fn': "isoInTPC_v5filesNew/isoInTPC_to1500MeV_p_v5_dEdxAllTracksNoFile.root",
      'fn': "isoInTPC_v5filesNewNew/dEdxAllTracksNoFile_to1500MeV_p_v5.root",
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

  histConfigs = [
    {
      'name': "startx",
      'xtitle': "x [cm]",
      'ytitle': "Events / bin",
      'binning': [100,-10,60],
      'var': "true_startPosX",
      'cuts': "",
    },
    {
      'name': "endx",
      'xtitle': "x [cm]",
      'ytitle': "Events / bin",
      'binning': [100,-10,60],
      'var': "true_endPosX",
      'cuts': "",
    },
    {
      'name': "starty",
      'xtitle': "y [cm]",
      'ytitle': "Events / bin",
      'binning': [100,-30,30],
      'var': "true_startPosY",
      'cuts': "",
    },
    {
      'name': "endy",
      'xtitle': "y [cm]",
      'ytitle': "Events / bin",
      'binning': [100,-30,30],
      'var': "true_endPosY",
      'cuts': "",
    },
    {
      'name': "startz",
      'xtitle': "z [cm]",
      'ytitle': "Events / bin",
      'binning': [100,-10,100],
      'var': "true_startPosZ",
      'cuts': "",
    },
    {
      'name': "endz",
      'xtitle': "z [cm]",
      'ytitle': "Events / bin",
      'binning': [100,-10,100],
      'var': "true_endPosZ",
      'cuts': "",
    },
    {
      'name': "endyVendz",
      'xtitle': "z [cm]",
      'ytitle': "y [cm]",
      'binning': [100,-10,100,60,-30,30],
      'var': "true_endPosY:true_endPosZ",
      'cuts': "",
    },
    {
      'name': "endxVendz",
      'xtitle': "z [cm]",
      'ytitle': "x [cm]",
      'binning': [100,-10,100,70,-10,60],
      'var': "true_endPosX:true_endPosZ",
      'cuts': "",
    },
    {
      'name': "endyVendx",
      'xtitle': "x [cm]",
      'ytitle': "y [cm]",
      'binning': [70,-10,60,50,-30,30],
      'var': "true_endPosY:true_endPosX",
      'cuts': "",
    },
    # cuts
    {
      'name': "endyVendzBadLen",
      'xtitle': "z [cm]",
      'ytitle': "y [cm]",
      'binning': [100,-10,100,60,-30,30],
      'var': "true_endPosY:true_endPosZ",
      'cuts': "resRange[0]/true_resRange[0] < 0.5",
    },
    {
      'name': "endxVendzBadLen",
      'xtitle': "z [cm]",
      'ytitle': "x [cm]",
      'binning': [100,-10,100,70,-10,60],
      'var': "true_endPosX:true_endPosZ",
      'cuts': "resRange[0]/true_resRange[0] < 0.5",
    },
    {
      'name': "endyVendxBadLen",
      'xtitle': "x [cm]",
      'ytitle': "y [cm]",
      'binning': [70,-10,60,50,-30,30],
      'var': "true_endPosY:true_endPosX",
      'cuts': "resRange[0]/true_resRange[0] < 0.5",
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree",outPrefix="checkpos_")

  histConfigs = [
    {
      'name': "lengthVtrueLength",
      'xtitle': "True length [cm]",
      'ytitle': "Track length [cm]",
      'binning': [100,0,50,100,0,50],
      'var': "resRange[0]:true_resRange[0]",
      'cuts': "",
    },
    {
      'name': "lengthFrac",
      'xtitle': "Track length / True length",
      'ytitle': "Events / bin",
      'binning': [100,0,2],
      'var': "resRange[0]/true_resRange[0]",
      'cuts': "",
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree",outPrefix="checklength_")

