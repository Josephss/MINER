#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <TMath.h>
#include <TCanvas.h>
#include <TPad.h>
#include <TH1D.h>

const Double_t X_MIN = 4000.; const Double_t X_MAX = 8000.; //fit borders

TCanvas *c_Spectrum = new TCanvas("c_Spectrum", "c_Spectrum", 640, 480);
TPad *p_Spectrum = new TPad("p_Spectrum", "p_Spectrum", 0.0, 0.0, 1, 1);
//TH1D *h_Spectrum = new TH1D("h_Spectrum", "Spectrum", 1001, 0.0, 1000.0);
TH1D *h_Spectrum = new TH1D("h_Spectrum", "Spectrum", 500, 0.0, 40000.0);

double arrCounts[1000];
using namespace std; 

void fit_histo_L()
{
  ifstream f_open; //stream class to write on files
//  f_open.open("241Am.dat"); //open the file
  f_open.open("project_Qchisq0_39.dat"); //open the file
  int x_val;
  for(int channel=0; channel<=500; channel++)
    {
       f_open >>x_val >>arrCounts[channel];
       //cout<<x_val<<"  "<<arrCounts[channel]<<endl; 
       h_Spectrum->Fill(x_val, arrCounts[channel]);
    }
  f_open.close();


//  ofstream f_save;
//  f_save.open("/mnt/e/SuperCDMS/ROOT_presentation/241Am_out.dat");
//  for(int i=0; i<=1000; i++){
//    int yVal=h_Spectrum->GetBinContent(i);
    //cout<<yVal<<endl;
//    f_save<<i<<"   "<<yVal<<endl;
//  }
//  f_save.close();

//  TF1 *fSignal = new TF1("fSignal", "gaus", X_MIN, X_MAX);
//  TF1 *fBackground = new TF1("fBackground", "pol0+expo(1)", X_MIN, X_MAX);
//  TF1 *fSpectrum = new TF1("fSpectrum", "gaus + pol0(3) + expo(4)", X_MIN, X_MAX);

//--------
  TF1 *fSignal = new TF1("fSignal", "landau", X_MIN, X_MAX);
  TF1 *fBackground = new TF1("fBackground", "expo(1)", X_MIN, X_MAX);
  TF1 *fSpectrum = new TF1("fSpectrum", "landau+expo(3)", X_MIN, X_MAX);


  fSpectrum->SetParNames("Amplitude", "Mean", "Sigma", "exp_1", "exp_2");
  fSpectrum->SetParameters(700, 4000, 50, 6, 0);

  h_Spectrum->Fit("fSpectrum", "", "", X_MIN, X_MAX);

  Double_t param[4]; fSpectrum->GetParameters(param);

                     fSignal->SetParameters(&param[0]);   
          	     fBackground->SetParameters(&param[2]);



//  cout<<param[0]<<" "<<param[1]<<" "<<param[2]<<" "<<param[3]<<" "<<param[4]<<endl;

  p_Spectrum->Draw(); p_Spectrum->cd();
  h_Spectrum->SetStats(kFALSE);     h_Spectrum->Draw(); h_Spectrum->GetXaxis()->SetRangeUser(0, 15000);
  h_Spectrum->SetStats(kFALSE);     h_Spectrum->SetLineColor(kBlue); 
  fSignal->SetLineColor(kBlack);    fSignal->Draw("same");
  fBackground->SetLineColor(kBlue); fBackground->Draw("same"); 
  fSpectrum->Draw("same"); 
  
}
