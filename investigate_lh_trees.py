#!/usr/bin/env python

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)

# pip end processes: pi+Inelastic LArVoxelReadoutScoringProcess Decay
# p end processes: protonInelastic LArVoxelReadoutScoringProcess

#PRELIMINARYSTRING="LArIAT MC"
PRELIMINARYSTRING="LArIAT Simulation"

if __name__ == "__main__":
  c = root.TCanvas()

  fileConfigs = [
    {
      #'fn': "06_34_01_v1/new_pip_v1.root",
      #'fn': "06_34_01_v2/new_pip_v2.root",
      'fn': "06_34_01_v3/new_pip_v3.root",
      #'fn': "06_34_01_v4/new_pip_v4.root",
      'name': "pip",
      'title': "Isotropic #pi^{+}",
      'caption': "Isotropic #pi^{+}",
      'preliminaryString':PRELIMINARYSTRING,
    },
    {
      #'fn': "06_34_01_v1/new_p_v1.root",
      #'fn': "06_34_01_v2/new_p_v2.root",
      'fn': "06_34_01_v3/new_p_v3.root",
      #'fn': "06_34_01_v4/new_p_v4.root",
      'name': "p",
      'title': "Isotropic Proton",
      'caption': "Isotropic Proton",
      'preliminaryString':PRELIMINARYSTRING,
    },
  ]
  for i in range(len(fileConfigs)):
    fileConfigs[i]['color'] = COLORLIST[i]

  histConfigs = [
    {
      'name': "trkLen",
      'xtitle': "Track Length [cm]",
      'ytitle': "Events/bin",
      'binning': [90,0.,90],
      'var': "trkLen",
      'cuts': "",
      #'normalize': True,
      'preliminaryString':PRELIMINARYSTRING,
    },
    {
      'name': "true_length",
      'xtitle': "True Trajectory Length [cm]",
      'ytitle': "Events/bin",
      'binning': [100,0.,100],
      'var': "true_length",
      'cuts': "",
      #'normalize': True,
      'preliminaryString':PRELIMINARYSTRING,
    },
    {
      'name': "true_p",
      'xtitle': "Generated Momentum [MeV/c]",
      'ytitle': "Events/bin",
      'binning': [200,0.,2000],
      'var': "true_p*1000.",
      'cuts': "",
      #'normalize': True,
      'preliminaryString':PRELIMINARYSTRING,
    },
    {
      'name': "true_KE",
      'xtitle': "Generated Kinetic Energy [MeV]",
      'ytitle': "Events/bin",
      'binning': [100,0.,1000.],
      'var': "(true_E-sqrt(pow(true_E,2)-pow(true_p,2)))*1000.",
      'cuts': "",
      #'normalize': True,
      'preliminaryString':PRELIMINARYSTRING,
    },
  ]
  plotManyFilesOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="LHSample_")

  histConfigs = [
    {
      'name': "trkLenVtrue_p",
      'ytitle': "Track Length [cm]",
      'xtitle': "Generated Momentum [MeV/c]",
      'binning': [100,0.,1000.,100,0.,100],
      'var': "trkLen:true_p*1000.",
      'cuts': "",
      #'normalize': True,
    },
    {
      'name': "true_lengthVtrue_p",
      'ytitle': "True Trajectory Length [cm]",
      'xtitle': "Generated Momentum [MeV/c]",
      'binning': [100,0.,1000.,100,0.,100],
      'var': "true_length:true_p*1000.",
      'cuts': "",
      #'normalize': True,
    },
    {
      'name': "true_lengthVtrue_KE",
      'ytitle': "True Trajectory Length [cm]",
      'xtitle': "Generated Kinetic Energy [MeV]",
      'binning': [100,0.,1000.,100,0.,100],
      'var': "true_length:(true_E-sqrt(pow(true_E,2)-pow(true_p,2)))*1000.",
      'cuts': "",
      #'normalize': True,
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="LHSample_")

  ## All Truth Tree!!!
  histConfigs = [
    {
      'name': "true_lengthVtrue_p",
      'ytitle': "True Trajectory Length [cm]",
      'xtitle': "Generated Momentum [MeV/c]",
      'binning': [100,0.,1000.,100,0.,100],
      'var': "true_length:true_p*1000.",
      'cuts': "true_endContained",
      #'normalize': True,
    },
    {
      'name': "true_lengthVtrue_KE",
      'ytitle': "True Trajectory Length [cm]",
      'xtitle': "Generated Kinetic Energy [MeV]",
      'binning': [100,0.,1000.,100,0.,100],
      'var': "true_length:(true_E-sqrt(pow(true_E,2)-pow(true_p,2)))*1000.",
      'cuts': "true_endContained",
      #'normalize': True,
    },
  ]
  plotOneHistOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/alltruth",outPrefix="LHSampleAllTruth_")

  # Comparing end process Length
  histConfigs = [
    {
      'title': "All",
      'xtitle': "True Trajectory Length [cm]",
      'ytitle': "Events/bin",
      'binning': [100,0.,100],
      'var': "true_length",
      'cuts': "",
      #'normalize': True,
    },
    {
      'title': "Inelastic",
      'xtitle': "True Trajectory Length [cm]",
      'ytitle': "Events/bin",
      'binning': [100,0.,100],
      'var': "true_length",
      'cuts': '(true_endProcess == "pi+Inelastic" || true_endProcess == "protonInelastic")',
      #'normalize': True,
    },
    {
      'title': "Stopping",
      'xtitle': "True Trajectory Length [cm]",
      'ytitle': "Events/bin",
      'binning': [100,0.,100],
      'var': "true_length",
      'cuts': '(true_endProcess == "LArVoxelReadoutScoringProcess")',
      #'normalize': True,
    },
    {
      'title': "Decay",
      'xtitle': "True Trajectory Length [cm]",
      'ytitle': "Events/bin",
      'binning': [100,0.,100],
      'var': "true_length",
      'cuts': '(true_endProcess == "Decay")',
      #'normalize': True,
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]['color'] = COLORLIST[i]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="LHSampleEndProc_true_length")

  # Fraction end process Length
  histConfigs = [
    {
      'title': "Inelastic",
      'xtitle': "True Trajectory Length [cm]",
      'ytitle': "Fraction",
      'binning': [40,0.,100],
      'var': "true_length",
      'cuts': '(true_endProcess == "pi+Inelastic" || true_endProcess == "protonInelastic")',
      'efficiencyDenomCuts': '',
      #'normalize': True,
    },
    {
      'title': "Stopping",
      'xtitle': "True Trajectory Length [cm]",
      'ytitle': "Fraction",
      'binning': [40,0.,100],
      'var': "true_length",
      'cuts': '(true_endProcess == "LArVoxelReadoutScoringProcess")',
      'efficiencyDenomCuts': '',
      #'normalize': True,
    },
    {
      'title': "Decay",
      'xtitle': "True Trajectory Length [cm]",
      'ytitle': "Fraction",
      'binning': [40,0.,100],
      'var': "true_length",
      'cuts': '(true_endProcess == "Decay")',
      'efficiencyDenomCuts': '',
      #'normalize': True,
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]['color'] = COLORLIST[i+1]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="LHSampleEndProcFrac_true_length")

  # Comparing end process KE
  histConfigs = [
    {
      'title': "All",
      'xtitle': "Generated Kinetic Energy [MeV]",
      'ytitle': "Events/bin",
      'binning': [100,0.,1000],
      'var': "(true_E-sqrt(pow(true_E,2)-pow(true_p,2)))*1000.",
      'cuts': "",
      #'normalize': True,
    },
    {
      'title': "Inelastic",
      'xtitle': "Generated Kinetic Energy [MeV]",
      'ytitle': "Events/bin",
      'binning': [100,0.,1000],
      'var': "(true_E-sqrt(pow(true_E,2)-pow(true_p,2)))*1000.",
      'cuts': '(true_endProcess == "pi+Inelastic" || true_endProcess == "protonInelastic")',
      #'normalize': True,
    },
    {
      'title': "Stopping",
      'xtitle': "Generated Kinetic Energy [MeV]",
      'ytitle': "Events/bin",
      'binning': [100,0.,1000],
      'var': "(true_E-sqrt(pow(true_E,2)-pow(true_p,2)))*1000.",
      'cuts': '(true_endProcess == "LArVoxelReadoutScoringProcess")',
      #'normalize': True,
    },
    {
      'title': "Decay",
      'xtitle': "Generated Kinetic Energy [MeV]",
      'ytitle': "Events/bin",
      'binning': [100,0.,1000],
      'var': "(true_E-sqrt(pow(true_E,2)-pow(true_p,2)))*1000.",
      'cuts': '(true_endProcess == "Decay")',
      #'normalize': True,
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]['color'] = COLORLIST[i]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="LHSampleEndProc_true_KE")

  # Fraction end process KE
  histConfigs = [
    {
      'title': "Inelastic",
      'xtitle': "Generated Kinetic Energy [MeV]",
      'ytitle': "Fraction",
      'binning': [40,0.,1000],
      'var': "(true_E-sqrt(pow(true_E,2)-pow(true_p,2)))*1000.",
      'cuts': '(true_endProcess == "pi+Inelastic" || true_endProcess == "protonInelastic")',
      'efficiencyDenomCuts': '',
      #'normalize': True,
    },
    {
      'title': "Stopping",
      'xtitle': "Generated Kinetic Energy [MeV]",
      'ytitle': "Fraction",
      'binning': [40,0.,1000],
      'var': "(true_E-sqrt(pow(true_E,2)-pow(true_p,2)))*1000.",
      'cuts': '(true_endProcess == "LArVoxelReadoutScoringProcess")',
      'efficiencyDenomCuts': '',
      #'normalize': True,
    },
    {
      'title': "Decay",
      'xtitle': "Generated Kinetic Energy [MeV]",
      'ytitle': "Fraction",
      'binning': [40,0.,1000],
      'var': "(true_E-sqrt(pow(true_E,2)-pow(true_p,2)))*1000.",
      'cuts': '(true_endProcess == "Decay")',
      'efficiencyDenomCuts': '',
      #'normalize': True,
    },
  ]
  for i in range(len(histConfigs)):
    histConfigs[i]['color'] = COLORLIST[i+1]
  plotManyHistsOnePlot(fileConfigs,histConfigs,c,"likelihoodpidmaker/tree",outPrefix="LHSampleEndProcFrac_true_KE")
