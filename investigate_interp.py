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
      'fn': "06_06_06v1/likelihood_protoDUNE_p_v1.root",
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
      'name': "dEdxVRange_endsInelastic",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': 'plane==1 && true_endProcess == "protonInelastic"',
      #'normalize': True,
      'caption': "True EndProcess = protonInelastic"
    },
    {
      'name': "dEdxVRange_notEndsInelastic",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': 'plane==1 && true_endProcess != "protonInelastic"',
      #'normalize': True,
      'caption': "True EndProcess #neq protonInelastic"
    },
    {
      'name': "dEdxVRange_endsInelastic_plt750",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': 'plane==1 && true_endProcess == "protonInelastic" && true_p < 0.75',
      #'normalize': True,
      'caption': "True EndProcess = protonInelastic, p < 750 MeV/c"
    },
    {
      'name': "dEdxVRange_notEndsInelastic_plt750",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': 'plane==1 && true_endProcess != "protonInelastic" && true_p < 0.75',
      #'normalize': True,
      'caption': "True EndProcess #neq protonInelastic, p < 750 MeV/c"
    },
    {
      'name': "dEdxVRange_endsInelastic_pgt750",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': 'plane==1 && true_endProcess == "protonInelastic" && true_p > 0.75',
      #'normalize': True,
      'caption': "True EndProcess = protonInelastic, p > 750 MeV/c"
    },
    {
      'name': "dEdxVRange_notEndsInelastic_pgt750",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': 'plane==1 && true_endProcess != "protonInelastic" && true_p > 0.75',
      #'normalize': True,
      'caption': "True EndProcess #neq protonInelastic, p > 750 MeV/c"
    },
    {
      'name': "dEdxVRange_trkLengthlt0p5",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && resRange[0]/true_resRange[0] < 0.5",
      #'normalize': True,
      'caption': "Track Length < 50#% of True Trajectory Length"
    },
    {
      'name': "dEdxVRange_trkLengthgt0p5",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && resRange[0]/true_resRange[0] > 0.5",
      #'normalize': True,
      'caption': "Track Length > 50#% of True Trajectory Length"
    },
    {
      'name': "dEdxVRange_trkLengthlt1p25",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && resRange[0]/true_resRange[0] < 1.25",
      #'normalize': True,
      'caption': "Track Length < 125#% of True Trajectory Length"
    },
    {
      'name': "dEdxVRange_interpDistancelt1cm",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && interpDistance < 1.",
      #'normalize': True,
      'caption': "Hit less than 1cm from true trajectory"
    },
    {
      'name': "dEdxVRange_elasticEvent",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && @true_trajProcIs.size() > 0",
      #'normalize': True,
      'caption': "Elestic Scatter Present"
    },
    {
      'name': "dEdxVRange_NotElasticEvent",
      'xtitle': "Residual range [cm]",
      'ytitle': "dE/dx [MeV/cm]",
      'binning': [100,0.,15.,30,0.,30.],
      'var': "dEdx_raw:resRange",
      'cuts': "plane==1 && @true_trajProcIs.size() == 0",
      #'normalize': True,
      'caption': "No Elestic Scatter Present"
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
      'binning': [200,0.,2000,300,0,30],
      'var': "dEdx_raw:interpP*1000",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "dEdxVinterpP_interpDistancelt1cm",
      'xtitle': "Interpolated True Momentum [MeV/c]",
      'ytitle': "Reco dE/dx [MeV/cm]",
      'binning': [200,0.,2000,300,0,30],
      'var': "dEdx_raw:interpP*1000",
      'cuts': "plane==1 && interpDistance < 1.",
      #'normalize': True,
      'caption': "Hit less than 1cm from true trajectory"
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
      'name': "dEdxVinterpKE_interpDistancelt1cm",
      'xtitle': "Interpolated True Kinetic Energy [MeV]",
      'ytitle': "Reco dE/dx [MeV/cm]",
      'binning': [100,0.,1000.,30,0,30],
      'var': "dEdx_raw:interpE*1000-938.27",
      'cuts': "plane==1 && interpDistance < 1.",
      #'normalize': True,
      'caption': "Hit less than 1cm from true trajectory"
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
      'name': "interpDistanceToClosestTrajPoint",
      'xtitle': "Distance from Reco Hit to Nearest Trajectory Point [cm]",
      'ytitle': "Entries/bin",
      'binning': [100,0.,10],
      'var': "interpDistanceToClosestTrajPoint",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "matchStartDistance",
      'xtitle': "Distance from Start of Reco Track to Start of True Trajectory [cm]",
      'ytitle': "Entries/bin",
      'binning': [100,0.,10],
      'var': "matchStartDistance",
      'cuts': "",
      #'normalize': True,
    },
    {
      'name': "matchStartAngle",
      'xtitle': "Angle between Start of Reco Track to Start of True Trajectory [deg]",
      'ytitle': "Entries/bin",
      'binning': [180,0.,180],
      'var': "matchStartAngle*180/pi",
      'cuts': "",
      #'normalize': True,
    },
    {
      'name': "matchEndDistance",
      'xtitle': "Distance from End of Reco Track to End of True Trajectory [cm]",
      'ytitle': "Entries/bin",
      'binning': [100,0.,10],
      'var': "matchEndDistance",
      'cuts': "",
      #'normalize': True,
    },
    {
      'name': "matchEndAngle",
      'xtitle': "Angle between End of Reco Track to End of True Trajectory [deg]",
      'ytitle': "Entries/bin",
      'binning': [180,0.,180],
      'var': "matchEndAngle*180/pi",
      'cuts': "",
      #'normalize': True,
    },
    {
      'name': "interpPVtrueP",
      'binning': [200,0.,2000,200,0,2000],
      'ytitle': "Interpolated True Momentum [MeV/c]",
      'xtitle': "Initial True Momentum [MeV/c]",
      'var': "interpP*1000:true_p*1000",
      'cuts': "plane==1",
      #'normalize': True,
    },
    {
      'name': "trueTrajPVtrueP",
      'binning': [200,0.,2000,200,0,2000],
      'ytitle': "True Trajectory Momentum [MeV/c]",
      'xtitle': "Initial True Momentum [MeV/c]",
      'var': "true_trajp*1000:true_p*1000",
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
    {
      'name': "trueTrajProcI",
      'xtitle': "Interpolated True Kinetic Energy [MeV]",
      'ytitle': "Track Curveyness [deg]",
      'binning': [100,0.,1000,60,0,30],
      'var': "trkCurvyness*180/pi:interpE*1000-938.27",
      'cuts': "plane==1",
      #'normalize': True,
    },
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
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="checkinterp_")

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
      'binning': [100,0,30],
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
      'binning': [100,0,30],
      'var': "dEdx_raw",
      'cuts': "plane==1 && interpE*1000-938.27 > 100.",
      'normalize': True,
    },
  ]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="checkinterpdEdx_")

  histConfigs = [
    {
      'name': "KEleq1MeV",
      'title': "KE #leq 1 MeV",
      'xtitle': "Distance to True Trajectory [cm]",
      'ytitle': "Entries/cm",
      'binning': getLogBins(20,0.01,10),
      'var': "interpDistance",
      'cuts': "plane==1 && interpE*1000-938.27 <= 1",
      #'normalize': True,
      'color': root.kRed,
      'normToBinWidth': True,
      'logx': True,
      'logy': True,
    },
    {
      'name': "KEleq1MeVbasd",
      'title': "1 MeV < KE #leq 100 MeV",
      'xtitle': "Distance to True Trajectory [cm]",
      'ytitle': "Entries/cm",
      'binning': getLogBins(20,0.01,10),
      'var': "interpDistance",
      'cuts': "plane==1 && interpE*1000-938.27 >1 && interpE*1000-938.27 <= 100",
      #'normalize': True,
      'color': root.kBlue,
      'normToBinWidth': True,
      'logx': True,
      'logy': True,
    },
    {
      'name': "KEgt1MeV",
      'title': "KE > 100 MeV",
      'xtitle': "Distance to True Trajectory [cm]",
      'ytitle': "Entries/cm",
      'binning': getLogBins(20,0.01,10),
      'var': "interpDistance",
      'cuts': "plane==1 && interpE*1000-938.27 > 100.",
      #'normalize': True,
      'normToBinWidth': True,
      'logx': True,
      'logy': True,
    },
  ]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="checksmallKE_interpDistance")

  histConfigs = [
    {
      'name': "KEleq1MeV",
      'title': "KE #leq 1 MeV",
      'xtitle': "Distance to Nearest True Trajectory Point [cm]",
      'ytitle': "Normalized entries/bin",
      'binning': [30,0,30],
      'var': "interpDistanceToClosestTrajPoint",
      'cuts': "plane==1 && interpE*1000-938.27 <= 1",
      'normalize': True,
      'color': root.kRed,
    },
    {
      'name': "KEleq1MeVbasd",
      'title': "1 MeV < KE #leq 100 MeV",
      'xtitle': "Distance to Nearest True Trajectory Point [cm]",
      'ytitle': "Normalized entries/bin",
      'binning': [30,0,30],
      'var': "interpDistanceToClosestTrajPoint",
      'cuts': "plane==1 && interpE*1000-938.27 >1 && interpE*1000-938.27 <= 100",
      'normalize': True,
      'color': root.kBlue,
    },
    {
      'name': "KEgt1MeV",
      'title': "KE > 100 MeV",
      'xtitle': "Distance to Nearest True Trajectory Point [cm]",
      'ytitle': "Normalized entries/bin",
      'binning': [30,0,30],
      'var': "interpDistanceToClosestTrajPoint",
      'cuts': "plane==1 && interpE*1000-938.27 > 100.",
      'normalize': True,
    },
  ]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="checksmallKE_interpDistanceToClosestTrajPoint")

  histConfigs = [
    {
      'name': "KEleq1MeV",
      'title': "Inelastic",
      'xtitle': "Initial Momentum [MeV/c]",
      'ytitle': "Events/bin",
      'binning': [150,0,1500],
      'var': "true_p*1000",
      'cuts': 'true_endProcess == "protonInelastic"',
      #'normalize': True,
      'color': root.kRed,
    },
    {
      'name': "KEgt1MeV",
      'title': "Ionization",
      'xtitle': "Initial Momentum [MeV/c]",
      'ytitle': "Events/bin",
      'binning': [150,0,1500],
      'var': "true_p*1000",
      'cuts': 'true_endProcess != "protonInelastic"',
      #'normalize': True,
    },
  ]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="checkEndProcess_trueP")
  histConfigs = [
    {
      'name': "KEleq1MeV",
      'title': "Inelastic",
      'xtitle': "Initial Kinetic Energy [MeV]",
      'ytitle': "Events/bin",
      'binning': [100,0,1000],
      'var': "true_E*1000-938.27",
      'cuts': 'true_endProcess == "protonInelastic"',
      #'normalize': True,
      'color': root.kRed,
    },
    {
      'name': "KEgt1MeV",
      'title': "Ionization",
      'xtitle': "Initial Kinetic Energy [MeV]",
      'ytitle': "Events/bin",
      'binning': [100,0,1000],
      'var': "true_E*1000-938.27",
      'cuts': 'true_endProcess != "protonInelastic"',
      #'normalize': True,
    },
  ]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="checkEndProcess_trueKE")
