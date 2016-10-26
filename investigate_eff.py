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
*Br    8 :interpDistanceToClosestTrajPoint : vector<float>                   *
*Br    9 :interpIClosestTrajPoint : vector<unsigned int>                     *
*Br   10 :KE        : KE/F                                                   *
*Br   11 :nCaloHits : nCaloHits/i                                            *
*Br   12 :pdg       : pdg/I                                                  *
*Br   13 :startPosX : startPosX/F                                            *
*Br   14 :startPosY : startPosY/F                                            *
*Br   15 :startPosZ : startPosZ/F                                            *
*Br   16 :endPosX   : endPosX/F                                              *
*Br   17 :endPosY   : endPosY/F                                              *
*Br   18 :endPosZ   : endPosZ/F                                              *
*Br   19 :trkCurvyness : trkCurvyness/F                                      *
*Br   20 :matchStartDistance : matchStartDistance/F                          *
*Br   21 :matchStartAngle : matchStartAngle/F                                *
*Br   22 :matchEndDistance : matchEndDistance/F                              *
*Br   23 :matchEndAngle : matchEndAngle/F                                    *
*Br   24 :true_resRange : vector<float>                                      *
*Br   25 :true_dEdx : vector<float>                                          *
*Br   26 :true_trajE : vector<float>                                         *
*Br   27 :true_trajp : vector<float>                                         *
*Br   28 :true_inTPC : vector<bool>                                          *
*Br   29 :true_trajProcIs : vector<unsigned int>                             *
*Br   30 :true_trajProcNames : vector<string>                                *
*Br   31 :nTruePoints : nTruePoints/i                                        *
*Br   32 :true_ELostInTPC : true_ELostInTPC/F                                *
*Br   33 :true_E    : true_E/F                                               *
*Br   34 :true_p    : true_p/F                                               *
*Br   35 :true_thetaZenith : true_thetaZenith/F                              *
*Br   36 :true_thetaYZ : true_thetaYZ/F                                      *
*Br   37 :true_thetaYX : true_thetaYX/F                                      *
*Br   38 :true_startPosX : true_startPosX/F                                  *
*Br   39 :true_startPosY : true_startPosY/F                                  *
*Br   40 :true_startPosZ : true_startPosZ/F                                  *
*Br   41 :true_endPosX : true_endPosX/F                                      *
*Br   42 :true_endPosY : true_endPosY/F                                      *
*Br   43 :true_endPosZ : true_endPosZ/F                                      *
*Br   44 :true_process : string                                              *
*Br   45 :true_endProcess : string                                           *
"""
if __name__ == "__main__":
  c = root.TCanvas()

  fileConfigs = [
    {
      'fn': "06_06_01_v2_likelihoodv2.4/likelihoodv2_to1500MeV_p_v2.root",
      'name': "",
    },
  ]
  histConfigs = [
    {
      'name': "LengthOverTrueLength",
      'xtitle': "Track Length / True Trajectory Length",
      'ytitle': "Events/bin",
      'binning': [100,0.,2.],
      'var': "resRange[0]/true_resRange[0]",
      'cuts': "",
      #'normalize': True,
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"dEdxAllTracksNoFile/tree",outPrefix="checkinterp_")
