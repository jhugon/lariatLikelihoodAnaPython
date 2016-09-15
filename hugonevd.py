#!/usr/bin/env python

"""
TFile**     anatree/AnaTree_single_isoInTPC_p_v5.txt.root   
 TFile*     anatree/AnaTree_single_isoInTPC_p_v5.txt.root   
  KEY: TDirectoryFile   anatree;1   anatree (AnaTreeT1034) folder
root [2] _file0.cd("anatree")
(Bool_t)1
root [3] _file0.ls()
TFile**     anatree/AnaTree_single_isoInTPC_p_v5.txt.root   
 TFile*     anatree/AnaTree_single_isoInTPC_p_v5.txt.root   
  TDirectoryFile*       anatree anatree (AnaTreeT1034) folder
   KEY: TTree   anatree;1   analysis tree
  KEY: TDirectoryFile   anatree;1   anatree (AnaTreeT1034) folder
root [4] anatree.Print()
*Br    0 :run       : run/I                                                  *
*Br    1 :subrun    : subrun/I                                               *
*Br    2 :event     : event/I                                                *
*Br    3 :evttime   : evttime/D                                              *
*Br    4 :efield    : efield[3]/D                                            *
*Br    5 :t0        : t0/I                                                   *
*Br    6 :nclus     : nclus/I                                                *
*Br    7 :clustertwire : clustertwire[nclus]/D                               *
*Br    8 :clusterttick : clusterttick[nclus]/D                               *
*Br    9 :cluendwire : cluendwire[nclus]/D                                   *
*Br   10 :cluendtick : cluendtick[nclus]/D                                   *
*Br   11 :cluplane  : cluplane[nclus]/I                                      *
*Br   12 :ntracks_reco : ntracks_reco/I                                      *
*Br   13 :trkvtxx   : trkvtxx[ntracks_reco]/D                                *
*Br   14 :trkvtxy   : trkvtxy[ntracks_reco]/D                                *
*Br   15 :trkvtxz   : trkvtxz[ntracks_reco]/D                                *
*Br   16 :trkendx   : trkendx[ntracks_reco]/D                                *
*Br   17 :trkendy   : trkendy[ntracks_reco]/D                                *
*Br   18 :trkendz   : trkendz[ntracks_reco]/D                                *
*Br   19 :trkstartdcosx : trkstartdcosx[ntracks_reco]/D                      *
*Br   20 :trkstartdcosy : trkstartdcosy[ntracks_reco]/D                      *
*Br   21 :trkstartdcosz : trkstartdcosz[ntracks_reco]/D                      *
*Br   22 :trkenddcosx : trkenddcosx[ntracks_reco]/D                          *
*Br   23 :trkenddcosy : trkenddcosy[ntracks_reco]/D                          *
*Br   24 :trkenddcosz : trkenddcosz[ntracks_reco]/D                          *
*Br   25 :trkWCtoTPCMath : trkWCtoTPCMath/I                                  *
*Br   26 :trklength : trklength[ntracks_reco]/D                              *
*Br   27 :trkmomrange : trkmomrange[ntracks_reco]/D                          *
*Br   28 :trkmommschi2 : trkmommschi2[ntracks_reco]/D                        *
*Br   29 :trkmommsllhd : trkmommsllhd[ntracks_reco]/D                        *
*Br   30 :ntrkhits  : ntrkhits[ntracks_reco]/I                               *
*Br   31 :trkx      : trkx[ntracks_reco][1000]/D                             *
*Br   32 :trky      : trky[ntracks_reco][1000]/D                             *
*Br   33 :trkz      : trkz[ntracks_reco][1000]/D                             *
*Br   34 :trkpitch  : trkpitch[ntracks_reco][2]/D                            *
*Br   35 :trkhits   : trkhits[ntracks_reco][2]/I                             *
*Br   36 :trkdedx   : trkdedx[ntracks_reco][2][1000]/D                       *
*Br   37 :trkrr     : trkrr[ntracks_reco][2][1000]/D                         *
*Br   38 :trkpitchhit : trkpitchhit[ntracks_reco][2][1000]/D                 *
*Br   39 :trkke     : trkke[ntracks_reco][2]/D                               *
*Br   40 :trkpida   : trkpida[ntracks_reco][2]/D                             *
*Br   41 :nTrajPoint : nTrajPoint[ntracks_reco]/I                            *
*Br   42 :pHat0_X   : pHat0_X[ntracks_reco][1000]/D                          *
*Br   43 :pHat0_Y   : pHat0_Y[ntracks_reco][1000]/D                          *
*Br   44 :pHat0_Z   : pHat0_Z[ntracks_reco][1000]/D                          *
*Br   45 :trjPt_X   : trjPt_X[ntracks_reco][1000]/D                          *
*Br   46 :trjPt_Y   : trjPt_Y[ntracks_reco][1000]/D                          *
*Br   47 :trjPt_Z   : trjPt_Z[ntracks_reco][1000]/D                          *
*Br   48 :trkg4id   : trkg4id[ntracks_reco]/I                                *
*Br   49 :primarytrkkey : primarytrkkey/I                                    *
*Br   50 :nhits     : nhits/I                                                *
*Br   51 :hit_plane : hit_plane[nhits]/I                                     *
*Br   52 :hit_wire  : hit_wire[nhits]/I                                      *
*Br   53 :hit_channel : hit_channel[nhits]/I                                 *
*Br   54 :hit_peakT : hit_peakT[nhits]/D                                     *
*Br   55 :hit_charge : hit_charge[nhits]/D                                   *
*Br   56 :hit_ph    : hit_ph[nhits]/D                                        *
*Br   57 :hit_tstart : hit_tstart[nhits]/D                                   *
*Br   58 :hit_tend  : hit_tend[nhits]/D                                      *
*Br   59 :hit_trkid : hit_trkid[nhits]/I                                     *
*Br   60 :hit_trkkey : hit_trkkey[nhits]/I                                   *
*Br   61 :hit_clukey : hit_clukey[nhits]/I                                   *
*Br   62 :hit_pk    : hit_pk[nhits]/I                                        *
*Br   63 :hit_t     : hit_t[nhits]/I                                         *
*Br   64 :hit_ch    : hit_ch[nhits]/I                                        *
*Br   65 :hit_fwhh  : hit_fwhh[nhits]/I                                      *
*Br   66 :hit_rms   : hit_rms[nhits]/D                                       *
*Br   67 :hit_nelec : hit_nelec[nhits]/D                                     *
*Br   68 :hit_energy : hit_energy[nhits]/D                                   *
*Br   69 :hit_dQds  : hit_dQds[nhits]/F                                      *
*Br   70 :hit_dEds  : hit_dEds[nhits]/F                                      *
*Br   71 :hit_ds    : hit_ds[nhits]/F                                        *
*Br   72 :hit_resrange : hit_resrange[nhits]/F                               *
*Br   73 :hit_x     : hit_x[nhits]/F                                         *
*Br   74 :hit_y     : hit_y[nhits]/F                                         *
*Br   75 :hit_z     : hit_z[nhits]/F                                         *
*Br   76 :nwctrks   : nwctrks/I                                              *
*Br   77 :wctrk_XFaceCoor : wctrk_XFaceCoor[nwctrks]/D                       *
*Br   78 :wctrk_YFaceCoor : wctrk_YFaceCoor[nwctrks]/D                       *
*Br   79 :wctrk_momentum : wctrk_momentum[nwctrks]/D                         *
*Br   80 :wctrk_theta : wctrk_theta[nwctrks]/D                               *
*Br   81 :wctrk_phi : wctrk_phi[nwctrks]/D                                   *
*Br   82 :wctrk_XDist : wctrk_XDist[nwctrks]/D                               *
*Br   83 :wctrk_YDist : wctrk_YDist[nwctrks]/D                               *
*Br   84 :wctrk_ZDist : wctrk_ZDist[nwctrks]/D                               *
*Br   85 :XWireHist : XWireHist[nwctrks][1000]/D                             *
*Br   86 :YWireHist : YWireHist[nwctrks][1000]/D                             *
*Br   87 :XAxisHist : XAxisHist[nwctrks][1000]/D                             *
*Br   88 :YAxisHist : YAxisHist[nwctrks][1000]/D                             *
*Br   89 :Y_Kink    : Y_Kink[nwctrks]/D                                      *
*Br   90 :ntof      : ntof/I                                                 *
*Br   91 :tofObject : tofObject[ntof]/D                                      *
*Br   92 :tof_timestamp : tof_timestamp[ntof]/D                              *
*Br   93 :nAG       : nAG/I                                                  *
*Br   94 :HitTimeStampUSE : HitTimeStampUSE[nAG]/D                           *
*Br   95 :HitTimeStampUSW : HitTimeStampUSW[nAG]/D                           *
*Br   96 :HitTimeStampDS1 : HitTimeStampDS1[nAG]/D                           *
*Br   97 :HitTimeStampDS2 : HitTimeStampDS2[nAG]/D                           *
*Br   98 :HitPulseAreaUSE : HitPulseAreaUSE[nAG]/F                           *
*Br   99 :HitPulseAreaUSW : HitPulseAreaUSW[nAG]/F                           *
*Br  100 :HitPulseAreaDS1 : HitPulseAreaDS1[nAG]/F                           *
*Br  101 :HitPulseAreaDS2 : HitPulseAreaDS2[nAG]/F                           *
*Br  102 :HitExistUSE : HitExistUSE[nAG]/O                                   *
*Br  103 :HitExistUSW : HitExistUSW[nAG]/O                                   *
*Br  104 :HitExistDS1 : HitExistDS1[nAG]/O                                   *
*Br  105 :HitExistDS2 : HitExistDS2[nAG]/O                                   *
*Br  106 :no_primaries : no_primaries/I                                      *
*Br  107 :geant_list_size : geant_list_size/I                                *
*Br  108 :pdg       : pdg[geant_list_size]/I                                 *
*Br  109 :Eng       : Eng[geant_list_size]/D                                 *
*Br  110 :Px        : Px[geant_list_size]/D                                  *
*Br  111 :Py        : Py[geant_list_size]/D                                  *
*Br  112 :Pz        : Pz[geant_list_size]/D                                  *
*Br  113 :EndEng    : EndEng[geant_list_size]/D                              *
*Br  114 :EndPx     : EndPx[geant_list_size]/D                               *
*Br  115 :EndPy     : EndPy[geant_list_size]/D                               *
*Br  116 :EndPz     : EndPz[geant_list_size]/D                               *
*Br  117 :StartPointx : StartPointx[geant_list_size]/D                       *
*Br  118 :StartPointy : StartPointy[geant_list_size]/D                       *
*Br  119 :StartPointz : StartPointz[geant_list_size]/D                       *
*Br  120 :EndPointx : EndPointx[geant_list_size]/D                           *
*Br  121 :EndPointy : EndPointy[geant_list_size]/D                           *
*Br  122 :EndPointz : EndPointz[geant_list_size]/D                           *
*Br  123 :Process   : Process[geant_list_size]/I                             *
*Br  124 :NumberDaughters : NumberDaughters[geant_list_size]/I               *
*Br  125 :Mother    : Mother[geant_list_size]/I                              *
*Br  126 :TrackId   : TrackId[geant_list_size]/I                             *
*Br  127 :process_primary : process_primary[geant_list_size]/I               *
*Br  128 :G4Process : vector<string>                                         *
*Br  129 :G4FinalProcess : vector<string>                                    *
*Br  130 :NTrTrajPts : NTrTrajPts[no_primaries]/I                            *
*Br  131 :MidPosX   : MidPosX[no_primaries][5000]/D                          *
*Br  132 :MidPosY   : MidPosY[no_primaries][5000]/D                          *
*Br  133 :MidPosZ   : MidPosZ[no_primaries][5000]/D                          *
*Br  134 :MidPx     : MidPx[no_primaries][5000]/D                            *
*Br  135 :MidPy     : MidPy[no_primaries][5000]/D                            *
*Br  136 :MidPz     : MidPz[no_primaries][5000]/D                            *
*Br  137 :no_mcshowers : no_mcshowers/I                                      *
*Br  138 :mcshwr_origin : mcshwr_origin[no_mcshowers]/D                      *
*Br  139 :mcshwr_pdg : mcshwr_pdg[no_mcshowers]/D                            *
*Br  140 :mcshwr_TrackId : mcshwr_TrackId[no_mcshowers]/I                    *
*Br  141 :mcshwr_startX : mcshwr_startX[no_mcshowers]/D                      *
*Br  142 :mcshwr_startY : mcshwr_startY[no_mcshowers]/D                      *
*Br  143 :mcshwr_startZ : mcshwr_startZ[no_mcshowers]/D                      *
*Br  144 :mcshwr_endX : mcshwr_endX[no_mcshowers]/D                          *
*Br  145 :mcshwr_endY : mcshwr_endY[no_mcshowers]/D                          *
*Br  146 :mcshwr_endZ : mcshwr_endZ[no_mcshowers]/D                          *
*Br  147 :mcshwr_CombEngX : mcshwr_CombEngX[no_mcshowers]/D                  *
*Br  148 :mcshwr_CombEngY : mcshwr_CombEngY[no_mcshowers]/D                  *
*Br  149 :mcshwr_CombEngZ : mcshwr_CombEngZ[no_mcshowers]/D                  *
*Br  150 :mcshwr_CombEngPx : mcshwr_CombEngPx[no_mcshowers]/D                *
*Br  151 :mcshwr_CombEngPy : mcshwr_CombEngPy[no_mcshowers]/D                *
*Br  152 :mcshwr_CombEngPz : mcshwr_CombEngPz[no_mcshowers]/D                *
*Br  153 :mcshwr_CombEngE : mcshwr_CombEngE[no_mcshowers]/D                  *
*Br  154 :mcshwr_dEdx : mcshwr_dEdx[no_mcshowers]/D                          *
*Br  155 :mcshwr_StartDirX : mcshwr_StartDirX[no_mcshowers]/D                *
*Br  156 :mcshwr_StartDirY : mcshwr_StartDirY[no_mcshowers]/D                *
*Br  157 :mcshwr_StartDirZ : mcshwr_StartDirZ[no_mcshowers]/D                *
*Br  158 :mcshwr_isEngDeposited : mcshwr_isEngDeposited[no_mcshowers]/I      *
*Br  159 :mcshwr_Motherpdg : mcshwr_Motherpdg[no_mcshowers]/I                *
*Br  160 :mcshwr_MotherTrkId : mcshwr_MotherTrkId[no_mcshowers]/I            *
*Br  161 :mcshwr_MotherstartX : mcshwr_MotherstartX[no_mcshowers]/I          *
*Br  162 :mcshwr_MotherstartY : mcshwr_MotherstartY[no_mcshowers]/I          *
*Br  163 :mcshwr_MotherstartZ : mcshwr_MotherstartZ[no_mcshowers]/I          *
*Br  164 :mcshwr_MotherendX : mcshwr_MotherendX[no_mcshowers]/I              *
*Br  165 :mcshwr_MotherendY : mcshwr_MotherendY[no_mcshowers]/I              *
*Br  166 :mcshwr_MotherendZ : mcshwr_MotherendZ[no_mcshowers]/I              *
*Br  167 :mcshwr_Ancestorpdg : mcshwr_Ancestorpdg[no_mcshowers]/I            *
*Br  168 :mcshwr_AncestorTrkId : mcshwr_AncestorTrkId[no_mcshowers]/I        *
*Br  169 :mcshwr_AncestorstartX : mcshwr_AncestorstartX[no_mcshowers]/I      *
*Br  170 :mcshwr_AncestorstartY : mcshwr_AncestorstartY[no_mcshowers]/I      *
*Br  171 :mcshwr_AncestorstartZ : mcshwr_AncestorstartZ[no_mcshowers]/I      *
*Br  172 :mcshwr_AncestorendX : mcshwr_AncestorendX[no_mcshowers]/I          *
*Br  173 :mcshwr_AncestorendY : mcshwr_AncestorendY[no_mcshowers]/I          *
*Br  174 :mcshwr_AncestorendZ : mcshwr_AncestorendZ[no_mcshowers]/I          *
*Br  175 :nshowers  : nshowers/I                                             *
*Br  176 :shwID     : shwI[nshowers]/I                                       *
*Br  177 :BestPlaneShw : BestPlaneShw[nshowers]/I                            *
*Br  178 :LengthShw : LengthShw[nshowers]/D                                  *
*Br  179 :CosStartShw : CosStartShw[3][1000]/D                               *
*Br  180 :CosStartXYZShw : CosStartXYZShw[3][1000]/D                         *
*Br  181 :TotalEShw : TotalEShw[2][1000]/D                                   *
*Br  182 :dEdxPerPlaneShw : dEdxPerPlaneShw[2][1000]/D                       *
*Br  183 :TotalMIPEShw : TotalMIPEShw[2][1000]/D                             *
"""

import ROOT as root
from helpers import *
root.gROOT.SetBatch(True)
from matplotlib import pyplot as mpl

def hugonevd(fn,treename,nmax=100,plotSecondary=True):
  f = root.TFile(fn)
  tree = f.Get(treename)
  nEvents = tree.GetEntries()
  nEvents = min(nEvents,nmax)
  for iEvent in range(nEvents):
    tree.GetEntry(iEvent)
    fig, axs = mpl.subplots(nrows=2,sharex=True)
    axxz = axs[0]
    axyz = axs[1]
    axxz.set_ylabel("x [cm]")
    axyz.set_ylabel("y [cm]")
    axyz.set_xlabel("z [cm]")
    axxz.set_ylim(-0,50)
    axxz.set_xlim(-5,95)
    axyz.set_ylim(-25,25)
    axyz.set_xlim(-5,95)
    primaryContained = True
    primaryLength = -1.
    primaryP = -1.
    print("*********** iEvent: {0:6} ************".format(iEvent))
    iPrimary = 0
    plots = []
    for iParticle in range(tree.geant_list_size):
      if not abs(tree.pdg[iParticle]) > 100000 and not abs(tree.pdg[iParticle]) == 2112:
        x = []
        y = []
        z = []
        print("iParticle: {}".format(iParticle))
        print("  process_primary: {} pdg: {} E: {} ID: {}".format(tree.process_primary[iParticle],tree.pdg[iParticle],tree.Eng[iParticle],tree.TrackId[iParticle]))
        print("  start,end: ({:6.2f},{:6.2f},{:6.2f}) -> ({:6.2f},{:6.2f},{:6.2f})".format(tree.StartPointx[iParticle],tree.StartPointy[iParticle],tree.StartPointz[iParticle],tree.EndPointx[iParticle],tree.EndPointy[iParticle],tree.EndPointz[iParticle]))
        color = 'b'
        if tree.process_primary[iParticle]:
          primaryLength = 0.
          primaryP = (tree.Px[iParticle]**2+tree.Py[iParticle]**2+tree.Pz[iParticle]**2)**0.5
          for iHit in range(tree.NTrTrajPts[iPrimary]):
            iArrayIndex = iParticle+iHit
            if iArrayIndex > len(tree.MidPosX):
              raise Exception("iArrayIndex to large")
            print("    point: {:6.1f},{:6.1f},{:6.1f}".format(tree.MidPosX[iArrayIndex],tree.MidPosY[iArrayIndex],tree.MidPosZ[iArrayIndex]))
            x.append(tree.MidPosX[iArrayIndex])
            y.append(tree.MidPosY[iArrayIndex])
            z.append(tree.MidPosZ[iArrayIndex])
            if tree.MidPosZ[iArrayIndex] > 95 or tree.MidPosZ[iArrayIndex] < -5 \
                or tree.MidPosX[iArrayIndex] > 50 or tree.MidPosX[iArrayIndex] < 0 \
                or tree.MidPosY[iArrayIndex] > 25 or tree.MidPosY[iArrayIndex] < -25:
              primaryContained = False
            if iHit > 0:
              primaryLength += (\
                (tree.MidPosX[iArrayIndex] - tree.MidPosX[iArrayIndex-1])**2 \
                + (tree.MidPosY[iArrayIndex] - tree.MidPosY[iArrayIndex-1])**2 \
                + (tree.MidPosZ[iArrayIndex] - tree.MidPosZ[iArrayIndex-1])**2 \
              )**(0.5)
        else:
          color = 'r'
          x.append(tree.StartPointx[iParticle])
          y.append(tree.StartPointy[iParticle])
          z.append(tree.StartPointz[iParticle])
          x.append(tree.EndPointx[iParticle])
          y.append(tree.EndPointy[iParticle])
          z.append(tree.EndPointz[iParticle])
        if tree.process_primary[iParticle]:
          plots.append(axyz.plot(z[0],y[0],'ob'))
          plots.append(axxz.plot(z[0],x[0],'ob'))
          plots.append(axxz.plot(z,x,c=color))
          plots.append(axyz.plot(z,y,c=color))
          iPrimary += 1
        elif plotSecondary:
          plots.append(axxz.plot(z,x,c=color))
          plots.append(axyz.plot(z,y,c=color))
      
    if primaryContained:
      continue

    trkLength = -1.
    for iTrack in range(tree.ntracks_reco):
      x = []
      y = []
      z = []
      print("iTrack: {}".format(iTrack))
      print("  start,end: ({:6.2f},{:6.2f},{:6.2f}) -> ({:6.2f},{:6.2f},{:6.2f})".format(tree.trkvtxx[iTrack],tree.trkvtxy[iTrack],tree.trkvtxz[iTrack],tree.trkendx[iTrack],tree.trkendy[iTrack],tree.trkendz[iTrack]))
      print("  length: {:8.2f}, matched G4 ID: {}".format(tree.trklength[iTrack],tree.trkg4id[iTrack]))
      trkLength = tree.trklength[iTrack]
      for iHit in range(tree.ntrkhits[iTrack]):
        iArrayIndex = iTrack+iHit
        if iArrayIndex > len(tree.trkx):
          raise Exception("iArrayIndex to large")
        #print("    point: {:6.1f},{:6.1f},{:6.1f}".format(tree.trkx[iArrayIndex],tree.trky[iArrayIndex],tree.trkz[iArrayIndex]))
        x.append(tree.trkx[iArrayIndex])
        y.append(tree.trky[iArrayIndex])
        z.append(tree.trkz[iArrayIndex])
      plots.append(axxz.plot(z,x,'--k',lw=2))
      plots.append(axyz.plot(z,y,'--k',lw=2))
    fig.text(0.05,0.95,"Event: {}, p = {:.0f} MeV/c, primary true length: {:0.1f} cm, reco track length: {:.1f} cm".format(iEvent,primaryP*1000,primaryLength,trkLength),ha='left')
    fig.savefig("EVD_{}.png".format(iEvent))

if __name__ == "__main__":

  hugonevd("anatree/AnaTree_single_isoInTPC_to1500MeV_p_v5.txt.root","anatree/anatree")
  #hugonevd("anatree/AnaTree_single_isoInTPC_p_v5.txt.root","anatree/anatree")
  #hugonevd("anatree/AnaTree_single_isoInTPC_kp_v5.txt.root","anatree/anatree")
  #hugonevd("anatree/AnaTree_single_isoInTPC_mup_v5.txt.root","anatree/anatree")

