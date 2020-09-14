#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <TMath.h>
#include <TCanvas.h>
#include <TPad.h>
#include <TH1D.h>

const Double_t X_MIN = 10.; const Double_t X_MAX = 40000; //fit borders

TCanvas *c_Spectrum = new TCanvas("c_Spectrum", "c_Spectrum", 800, 800);
TPad *p_Spectrum = new TPad("p_Spectrum", "p_Spectrum", 0.0, 0.0, 1, 1);
TH1D *h_Spectrum = new TH1D("h_Spectrum", "Spectrum", 1001, 0.0, 1000.0);
double arrCounts[1001];
using namespace std; 

void histogram_fit()
{
  ifstream f_open; //stream class to write on files
  f_open.open("project_Qchisq0_39.dat"); //open the file
  for(int channel=0; channel<=500; channel++)
    {
       f_open >> arrCounts[channel]; h_Spectrum->Fill(channel, arrCounts[channel]);
    }
  f_open.close();

  TF1 *fSignal = new TF1("fSignal", "gaus", X_MIN, X_MAX);
  TF1 *fBackground = new TF1("fBackground", "expo(1)", X_MIN, X_MAX);
  TF1 *fSpectrum = new TF1("fSpectrum", "gaus + expo(3)", X_MIN, X_MAX);

  fSpectrum->SetParNames("Amplitude", "Mean", "Sigma", "exp_1", "exp_2");
  fSpectrum->SetParameters(700, 4000, 50, 6, 0);

  h_Spectrum->Fit("fSpectrum", "", "", X_MIN, X_MAX);

  Double_t param[6]; fSpectrum->GetParameters(param);
                     fSignal->SetParameters(&param[0]);   
          	     fBackground->SetParameters(&param[2]);

  p_Spectrum->Draw(); p_Spectrum->cd();
  h_Spectrum->SetStats(kFALSE); h_Spectrum->Draw(); h_Spectrum->GetXaxis()->SetRangeUser(0, 1500);
  h_Spectrum->SetStats(kFALSE); h_Spectrum->SetLineColor(kBlue); 
  fSignal->Draw("same");
  fBackground->Draw("same"); 
}
