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
*Br    5 :interpE   : vector<float>                                          *
*Br    6 :interpP   : vector<float>                                          *
*Br    7 :interpDistance : vector<float>                                     *
*Br    8 :KE        : KE/F                                                   *
*Br    9 :nCaloHits : nCaloHits/i                                            *
*Br   10 :pdg       : pdg/I                                                  *
*Br   11 :startPosX : startPosX/F                                            *
*Br   12 :startPosY : startPosY/F                                            *
*Br   13 :startPosZ : startPosZ/F                                            *
*Br   14 :endPosX   : endPosX/F                                              *
*Br   15 :endPosY   : endPosY/F                                              *
*Br   16 :endPosZ   : endPosZ/F                                              *
*Br   17 :trkCurvyness : trkCurvyness/F                                      *
*Br   18 :trkSqrdCurvyness : trkSqrdCurvyness/F                              *
*Br   19 :true_resRange : vector<float>                                      *
*Br   20 :true_dEdx : vector<float>                                          *
*Br   21 :true_inTPC : vector<bool>                                          *
*Br   22 :nTruePoints : nTruePoints/i                                        *
*Br   23 :true_ELostInTPC : true_ELostInTPC/F                                *
*Br   24 :true_E    : true_E/F                                               *
*Br   25 :true_p    : true_p/F                                               *
*Br   26 :true_thetaZenith : true_thetaZenith/F                              *
*Br   27 :true_thetaYZ : true_thetaYZ/F                                      *
*Br   28 :true_thetaYX : true_thetaYX/F                                      *
*Br   29 :true_startPosX : true_startPosX/F                                  *
*Br   30 :true_startPosY : true_startPosY/F                                  *
*Br   31 :true_startPosZ : true_startPosZ/F                                  *
*Br   32 :true_endPosX : true_endPosX/F                                      *
*Br   33 :true_endPosY : true_endPosY/F                                      *
*Br   34 :true_endPosZ : true_endPosZ/F                                      *
*Br   35 :true_process : string                                              *
*Br   36 :true_endProcess : string                                           *
"""
if __name__ == "__main__":
  c = root.TCanvas()

  fileConfigs = [
    {
      'fn': "06_06_01/dEdxAllTracksNoFileV2_to1500_p_v2.root",
      'name': "",
    },
  ]
  histConfigs = [
    {
      'name': "dEdxVRange",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "KEVtrueE",
      'xtitle': "True KE [MeV]",
      'ytitle': "KE Reco [MeV]",
      'binning': [100,0.,1000.,100,0,2000],
      'var': "KE:true_E*1000-938.27",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "dEdxVinterpP",
      'xtitle': "Interpolated True Momentum [MeV/c]",
      'ytitle': "Reco dE/dx [MeV/cm]",
      'binning': [150,0.,1500,30,0,30],
      'var': "dEdx_raw:interpP*1000",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "dEdxVinterpKE",
      'xtitle': "Interpolated True Kinetic Energy [MeV]",
      'ytitle': "Reco dE/dx [MeV/cm]",
      'binning': [100,0.,1000.,30,0,30],
      'var': "dEdx_raw:interpE*1000-938.27",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "dEdxVinterpKELow",
      'xtitle': "Interpolated True Kinetic Energy [MeV]",
      'ytitle': "Reco dE/dx [MeV/cm]",
      'binning': [100,0.,10.,30,0,30],
      'var': "dEdx_raw:interpE*1000-938.27",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "interpKE",
      'xtitle': "Interpolated True Kinetic Energy [MeV]",
      'ytitle': "Entries/bin",
      'binning': [100,0.,1000],
      'var': "interpE*1000-938.27",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "interpKE_logx",
      'xtitle': "Interpolated True Kinetic Energy [MeV]",
      'ytitle': "Entries/MeV",
      'binning': getLogBins(100,1e-4,1000),
      'var': "interpE*1000-938.27",
      'cuts': "plane==1",
      #'normalize': True,
      'normToBinWidth': True,
      'logx': True,
      'logy': True,
    },
    {
      'name': "interpDistance",
      'xtitle': "Distance from Reco Hit to True Trajectory [cm]",
      'ytitle': "Entries/bin",
      'binning': [100,0.,1],
      'var': "interpDistance",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "interpPVtrueP",
      'binning': [150,0,1500,150,0,1500],
      'ytitle': "Interpolated True Momentum [MeV/c]",
      'xtitle': "Initial True Momentum [MeV/c]",
      'var': "interpP*1000:true_p*1000",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "interpPVtrueP",
      'binning': [150,0,1500,150,0,1500],
      'ytitle': "Interpolated True Momentum [MeV/c]",
      'xtitle': "Initial True Momentum [MeV/c]",
      'var': "interpP*1000:true_p*1000",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "trkCurvynessVinterpKE",
      'xtitle': "Interpolated True Kinetic Energy [MeV]",
      'ytitle': "Track Curveyness [deg]",
      'binning': [100,0.,1000,60,0,30],
      'var': "trkCurvyness*180/pi:interpE*1000-938.27",
      'cuts': "plane==1",
      #'normalize': True,
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree",outPrefix="checkinterp_")

  histConfigs = [
    {
      'name': "KEleq1MeV",
      'title': "KE #leq 1 MeV",
      'xtitle': "Reco dE/dx [MeV/cm]",
      'ytitle': "Normalized entries/bin",
      'binning': [30,0,30],
      'var': "dEdx_raw",
      'cuts': "plane==1 && interpE*1000-938.27 <= 1",
      'normalize': True,
      'color': root.kRed,
    },
    {
      'name': "KEleq1MeVbasd",
      'title': "1 MeV < KE #leq 100 MeV",
      'xtitle': "Reco dE/dx [MeV/cm]",
      'ytitle': "Normalized entries/bin",
      'binning': [30,0,30],
      'var': "dEdx_raw",
      'cuts': "plane==1 && interpE*1000-938.27 >1 && interpE*1000-938.27 <= 100",
      'normalize': True,
      'color': root.kBlue,
    },
    {
      'name': "KEgt1MeV",
      'title': "KE > 100 MeV",
      'xtitle': "Reco dE/dx [MeV/cm]",
      'ytitle': "Normalized entries/bin",
      'binning': [30,0,30],
      'var': "dEdx_raw",
      'cuts': "plane==1 && interpE*1000-938.27 > 100.",
      'normalize': True,
    },
  ]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree",outPrefix="checkinterpdEdx_")
