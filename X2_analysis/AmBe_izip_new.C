void AmBe_izip_new() {


// import ROOT files 

TFile *f1 = new TFile("05190720_1825_RQ.root","read");
TFile *f2 = new TFile("05190720_1825_RQ.root","read");
TFile *f3 = new TFile("05190720_1825_RRQ.root","read");

//create an empty root files (based on our definition)
TFile *f4 = new TFile("Chivsqsum1.root","recreate");
TFile *f5 = new TFile("Chivsqsum2.root","recreate");
TFile *f6 = new TFile("Chivsphonon1.root","recreate");
TFile *f7 = new TFile("Chivsphonon2.root","recreate");

// Define histograms 

TH2F *hist1 = new TH2F("hist1","QS1OFchisq vs qsum1 for AmBe izip; qsum1(keV);QS1OFchisq",500,0,1000,500,0,40000);
TH2F *hist2 = new TH2F("hist2","QS2OFchisq vs qsum2 for AmBe izip; qsum2(keV);QS2OFchisq",300,0,500,500,0,40000);
TH2F *hist3 = new TH2F("hist3","PS1OFchisq vs ps1OF for AmBe izip; ps1OF(keV);PS1OFchisq",500,0,4000,1000,0,50000);
TH2F *hist4 = new TH2F("hist4","PS2OFchisq vs ptOF for AmBe izip; ptOF(keV);PS2OFchisq",500,0,1000,1000,0,50000);


/*
TH1F *Qsum1 = new TH1F("Qsum1","Charge distribution for side 1  ; Qsum1(keV); Counts",100,0,500);
TH1F *Qsum2 = new TH1F("Qsum2","Charge distribution for side 2; Qsum2(keV); Counts",100,0,500);
TH1F *Qsum3 = new TH1F("Qsum3","Charge distribution for side 2; Qsum2(keV); Counts",100,0,500);
TH1F *qsum = new TH1F("qsum","Charge distribution for izip zoomed in at[0,00]; qsum(keV); Counts(5 keV/bin)",100,0,500);
TH1F *qsum1 = new TH1F("qsum1","Charge distribution for izip; qsum1OF(keV); Counts",100,0,500);
TH1F *qsum2 = new TH1F("qsum2","Charge distribution for izip; qsumOF(keV); Counts",100,0,500);


TH1F *pt = new TH1F("pt","Phonon distribution for izip zoomed in at[0,500] ; ptOF(keV); Counts(5 keV/bin)",1000,0,500);
TH1F *pt1 = new TH1F("pt1","Phonon distribution for izip; ptOF(keV); Counts",1000,0,500);
TH1F *pt2 = new TH1F("pt2","Phonon distribution for izip; ptOF(keV); Counts",1000,0,500);
TH1F *pt3 = new TH1F("pt3","Phonon distribution for izip; ptOF(keV); Counts",1000,0,500);
TH1F *pt4 = new TH1F("pt4","Phonon distribution for izip; ptOF(keV); Counts",1000,0,500);
TH1F *pt5 = new TH1F("pt5","Phonon distribution for izip; ptOF(keV); Counts",1000,0,500);*/

auto legend = new TLegend(0.5,0.7,0.9,0.9);
auto legend1 = new TLegend(0.5,0.7,0.9,0.9);


TH1F *Qsum1 = new TH1F("Qsum1","Charge distribution for side 1  ; Qsum1(keV); Counts",500,0,4000);
TH1F *Qsum2 = new TH1F("Qsum2","Charge distribution for side 2; Qsum2(keV); Counts",500,0,4000);
TH1F *Qsum3 = new TH1F("Qsum3","Charge distribution for side 2; Qsum2(keV); Counts",500,0,4000);
TH1F *qsum = new TH1F("qsum","Charge distribution for izip; qsum(keV); Counts(4 keV/bin)",500,0,4000);
TH1F *qsum1 = new TH1F("qsum1","Charge distribution for izip; qsum1OF(keV); Counts",500,0,4000);
TH1F *qsum2 = new TH1F("qsum2","Charge distribution for izip; qsumOF(keV); Counts",500,0,4000);


TH1F *pt = new TH1F("pt","Phonon distribution for izip; ptOF(keV); Counts(4 keV/bin)",500,0,4000);
TH1F *pt1 = new TH1F("pt1","Phonon distribution for izip; ptOF(keV); Counts",500,0,4000);
TH1F *pt2 = new TH1F("pt2","Phonon distribution for izip; ptOF(keV); Counts",500,0,4000);
TH1F *pt3 = new TH1F("pt3","Phonon distribution for izip; ptOF(keV); Counts",500,0,4000);
TH1F *pt4 = new TH1F("pt4","Phonon distribution for izip; ptOF(keV); Counts",500,0,4000);
TH1F *pt5 = new TH1F("pt5","Phonon distribution for izip; ptOF(keV); Counts",500,0,4000);

// Define canvas

TCanvas *c1=new TCanvas("c1","test1",800,800);
TCanvas *c2=new TCanvas("c2","test2",800,800);
TCanvas *c3=new TCanvas("c3","test3",800,800);
TCanvas *c4=new TCanvas("c4","test4",800,800);
TCanvas *c5=new TCanvas("c5","test5",800,800);
TCanvas *c6=new TCanvas("c6","test6",800,800);

// TTree assign 

TDirectoryFile *dir1 = (TDirectoryFile*)f1->Get("rqDir");
TDirectoryFile *dir2 = (TDirectoryFile*)f2->Get("rqDir");
TDirectoryFile *dir3 = (TDirectoryFile*)f3->Get("rrqDir");


TTree *t1 = (TTree*)dir1->Get("zip1");
TTree *t2 = (TTree*)dir2->Get("eventTree");
TTree *t3 = (TTree*)dir3->Get("calibzip1");

// Make friend

t1->AddFriend(t2);
t2->AddFriend(t3);

//t1->Scan("PCS2OFchisq");


// Draw histogram

// Plot Charge chi-sq
c1->cd();
t1->Draw("QS1OFchisq:qsum1OF>>hist1","EventCategory!=1");
hist1->SetOption("colz");
hist1->GetZaxis()->SetRangeUser(0, 10);
hist1->GetYaxis()->SetMaxDigits(3);

c2->cd();
t1->Draw("QS2OFchisq:qsum2OF>>hist2","EventCategory!=1");
hist2->SetOption("colz");
hist2->GetZaxis()->SetRangeUser(0, 10);
hist2->GetYaxis()->SetMaxDigits(3);

// Plot Phonon chi-sq 

c3->cd();
t1->Draw("PS1OFchisq:ps1OF>>hist3","EventCategory!=1 && Empty==0");
hist3->SetOption("colz");
hist3->GetYaxis()->SetMaxDigits(3);
hist3->GetZaxis()->SetRangeUser(0, 10);

c4->cd();
t1->Draw("PS2OFchisq:ps2OF>>hist4","EventCategory!=1 && Empty==0");
hist4->SetOption("colz");
hist4->GetZaxis()->SetRangeUser(0, 10);
hist4->GetYaxis()->SetMaxDigits(3);

//Write histogram in root file -- "recreate" files ..
//move all the way to the bottom 
f4->cd();
hist1->Write();
f5->cd();
hist2->Write();
f6->cd();
hist3->Write();
f7->cd();
hist4->Write();


// qsum plots


c5->cd();
c5->SetLogy();
qsum->GetYaxis()->SetMaxDigits(3); //start with 100...

t1->Draw("qsum1OF+qsum2OF>>qsum");  /// no cut
t1->Draw("qsum1OF+qsum2OF>>qsum2","(EventCategory!=1)"); /// Notrandom cut // removes randoms-j

t1->Draw("qsum1OF+qsum2OF>>Qsum2","(Empty==0)");  /// NotEmpty cut
t1->Draw("qsum1OF+qsum2OF>>Qsum1","(QS1OFchisq <= 4108 + (-8.514)*qsum1OF + 0.256*(qsum1OF)**2) && (QS2OFchisq <= 4094 + 5.363*qsum2OF + 0.1708*(qsum2OF)**2) ");  /////Charge chisq cut

t1->Draw("qsum1OF+qsum2OF>>qsum1","(PCS2OFchisq <= 5123 + 50.4*ps2OF + (-0.2215)*(ps2OF)**2 + 0.0003558*(ps2OF)**2) && (PS1OFchisq <= 7523 + 0.2115*ps1OF + 0.003922*(ps1OF)**2)");   ////Phonon chisq cut

t1->Draw("qsum1OF+qsum2OF>>Qsum3","(qo2OF<= 17.23 + (0.1698 * qi2OF))");  /////charge radial cut
// overlay the histograms 
qsum->Draw();
qsum2->Draw("same");
Qsum2->Draw("same");
Qsum1->Draw("same");
qsum1->Draw("same");
Qsum3->Draw("same");

qsum->SetLineColor(kBlack);
Qsum1->SetLineColor(kRed);
Qsum2->SetLineColor(kViolet);
qsum1->SetLineColor(kGreen);
qsum2->SetLineColor(kBlue);
Qsum3->SetLineColor(kOrange);

qsum->SetStats(0);

legend->AddEntry(qsum,"no cut");
legend->AddEntry(qsum2,"NotRandom");
legend->AddEntry(Qsum2,"NotEmpty");
legend->AddEntry(qsum1,"Pchisq");
legend->AddEntry(Qsum1,"Qchisq");
legend->AddEntry(Qsum3,"Charge radial cut(S2)");
legend->Draw("same");
c5->SaveAs("qsum_all_cut.png");


// pt plots 

c6->cd();
c6->SetLogy();

t1->Draw("ptOF>>pt"); ///// no cut
t1->Draw("ptOF>>pt2" ,"(EventCategory!=1)");  ///// NotRandom cut
t1->Draw("ptOF>>pt4" ,"(Empty==0)");   /////// NotEmpty cut
t1->Draw("ptOF>>pt1","(PCS2OFchisq <= 5123 + 50.4*ps2OF + (-0.2215)*(ps2OF)**2 + 0.0003558*(ps2OF)**2) && (PS1OFchisq <= 7523 + 0.2115*ps1OF + 0.003922*(ps1OF)**2)");  /////// Phonon chisq cut
t1->Draw("ptOF>>pt3" ,"(QS2OFchisq <= 5424 + 14.64*qsum2OF + 0.02611*(qsum2OF)**2)&&(QS1OFchisq <= 5174 + 12.2*qsum1OF + 0.2176*(qsum1OF)**2)"); ///// charge chisq cut
t1->Draw("ptOF>>pt5" ,"(qo2OF<= 17.23 + (0.1698 * qi2OF))"); /////////charge radial cut 


pt->Draw();
pt2->Draw("same");
pt5->Draw("same");
pt3->Draw("same");
pt4->Draw("same");
pt1->Draw("same");


pt3->SetLineColor(kRed);
pt->SetLineColor(kBlack);
pt4->SetLineColor(kViolet);
pt1->SetLineColor(kGreen);
pt2->SetLineColor(kBlue);
pt5->SetLineColor(kOrange);

pt->SetStats(0);

legend1->AddEntry(pt,"no cut");
legend1->AddEntry(pt2,"NotRandom");
legend1->AddEntry(pt4,"NotEmpty");
legend1->AddEntry(pt1,"Pchisq");
legend1->AddEntry(pt3,"Qchisq");
legend1->AddEntry(pt5,"Radial cut(S2)");

legend1->Draw("same");
c6->SaveAs("pt_all_cuts.png");


}






























