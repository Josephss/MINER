import ROOT
from ROOT import kTeal,kRed,kGreen,kOrange,kOrange,kBlack,kDashed
import numpy as np
from array import array
import matplotlib.pyplot as plt

# import ROOT file 
f = ROOT.TFile.Open("Chivsqsum1.root","READ")

# draw canvas
Qchisq=ROOT.TCanvas("Qchisq","Qchisq",800,600)
Qchisq.SetGrid()
Qchisq.GetFrame().SetFillColor(21)
Qchisq.GetFrame().SetBorderSize(12)

# draw histogram
hist=f.Get("hist1")
##hist.Print("all")

#ID upper and lower bins
lbin=np.array([0,40,80,120,160,200,240,280])    # used as bin no
ubin=np.array([39.9,79.9,119.9,159.9,199,239,279,319])

bincent=(lbin+ubin)/2.0

#mean, standard deviation, and error arrays
mu,std=[],[]
ermu,erstd=[],[]

#chi-squared cut values
chiSqVals = []
chiSqVals2 = []

#cut efficiency
goodEventsPercent = []
recoilEnergy = []

for i in np.arange(len(lbin)):#len(lbin)
    
    project=ROOT.TH1D()
    ulimit=hist.GetXaxis().FindBin(ubin[i])
    llimit=hist.GetXaxis().FindBin(lbin[i])
    project=hist.ProjectionY("project",llimit,ulimit)
    C2=ROOT.TCanvas("C2","C2",800,600)
    C2.cd()
    project.Draw()
    project.SetTitle("Projection of QS1OFchisq in qsum1 [%d,%d]; QS1OFchisq;Counts"%(lbin[i],ubin[i]))
    C2.SaveAs("charge_chisq_s1/project_Qchisq%d_%d.gif"%(lbin[i],ubin[i]))

    ##print(project.Print("all")) ## to save to file from the console
    mu2=project.GetMean()
    std2=project.GetStdDev()
    if i == 0:
        fit5=ROOT.TF1("fit5","[0]*TMath::Landau(x,[1],[2])",4e3,4e4)
        fit6=ROOT.TF1("fit6","pol0(1)",4e3,4e4)
        fit4=ROOT.TF1("SuperPosition", "[0]*TMath::Landau(x,[1],[2])+pol0(3)",4e3,4e4) ##((mu2*2-std2)/3),4e4 ##pol0 + expo ##4.05e3,4e4 (improves the fit)
        fit4.SetParNames("Amplitude", "Mean", "Sigma", "pol_0")
        fit4.SetParameters(700, 4000, 50, 6) ##700, 4000, 50, 6
        project.Fit(fit4, "R+")
        
        fit5.SetParameters(fit4.GetParameters()[0],fit4.GetParameters()[1],fit4.GetParameters()[2])
        fit6.SetParameters(fit4.GetParameters()[3],fit4.GetParameters()[3])
        fit5.SetLineColor(1)
        fit5.SetLineStyle(5)
        fit6.SetLineColor(kGreen+2) 
        fit6.SetLineStyle(4)
        
        fit5.Draw("same")
        fit6.Draw("same")
        
        #binmax  = project.GetMaximumBin()
        #print("Maximum bin ... " + str(binmax))
        #print(" Maximum value ----- " + str(project.GetBinContent(binmax)))
        
        cutValue = .89e4
        #get number of good events
        xaxis = project.GetXaxis()
        binx = xaxis.FindBin(cutValue)
        goodEvents = project.Integral(1,binx)
        print("good events: " + str(goodEvents))
        
        #get total number of events
        bintotal = xaxis.GetNbins()
        allEvents = project.Integral(1,bintotal)
        print("all events: " + str(allEvents))   
        
        #percentage
        perc = goodEvents/allEvents
        goodEventsPercent.append(perc)
        print("percentage : " + str(perc))
        recoilEn = (lbin[i] + ubin[i])/2
        recoilEnergy.append(recoilEn)
        
        chiSqVals.append(cutValue)
        chiSqVals2=np.append(chiSqVals2,cutValue)
        norm1,mu1,std1=fit4.GetParameter(0),fit4.GetParameter(1),fit4.GetParameter(2)
        ermu1,erstd1=fit4.GetParError(1),fit4.GetParError(2)         
        mu,std=np.append(mu,mu1),np.append(std,std1)
        ermu,erstd=np.append(ermu,ermu1),np.append(erstd,erstd1)        
    if i == 1:
        fit5=ROOT.TF1("fit5","[0]*TMath::Landau(x,[1],[2])",4.2e3,4e4)
        fit6=ROOT.TF1("fit6","pol0(1)",4.2e3,4e4)
        fit4=ROOT.TF1("SuperPosition", "[0]*TMath::Landau(x,[1],[2])+pol0(3)",4.2e3,4e4) ##4.05e3,4e4)
        fit4.SetParNames("Amplitude", "Mean", "Sigma", "pol_0")
        fit4.SetParameters(500, 5500, 1000, 6)  ##500, 5500, 70, 6
        project.Fit(fit4,"R+") ##fit4, "","",4.2e3,4e4
        
        fit5.SetParameters(fit4.GetParameters()[0],fit4.GetParameters()[1],fit4.GetParameters()[2])
        fit6.SetParameters(fit4.GetParameters()[3],fit4.GetParameters()[3])
        fit5.SetLineColor(1)
        fit5.SetLineStyle(5)
        fit6.SetLineColor(kGreen+2) 
        fit6.SetLineStyle(4)
        
        fit5.Draw("same")
        fit6.Draw("same")
        
        #binmax  = project.GetMaximumBin()
        #print("Maximum bin ... " + str(binmax))
        #print(" ----- " + str(project.GetBinContent(binmax)))
        
        cutValue = 1e4
        #get number of good events
        xaxis = project.GetXaxis()
        binx = xaxis.FindBin(cutValue)
        goodEvents = project.Integral(1,binx)
        print("good events: " + str(goodEvents))
        
        #get total number of events
        bintotal = xaxis.GetNbins()
        allEvents = project.Integral(1,bintotal)
        print("all events: " + str(allEvents))   
        
        #percentage
        perc = goodEvents/allEvents
        goodEventsPercent.append(perc)
        recoilEn = (lbin[i] + ubin[i])/2
        recoilEnergy.append(recoilEn)
        
        chiSqVals.append(cutValue)
        chiSqVals2=np.append(chiSqVals2,cutValue)
        norm1,mu1,std1=fit4.GetParameter(0),fit4.GetParameter(1),fit4.GetParameter(2)
        ermu1,erstd1=fit4.GetParError(1),fit4.GetParError(2)  
        mu,std=np.append(mu,mu1),np.append(std,std1)
        ermu,erstd=np.append(ermu,ermu1),np.append(erstd,erstd1)        
    if i == 2:
        fit5=ROOT.TF1("fit5","[0]*TMath::Landau(x,[1],[2])",5.09e3,4e4)
        fit6=ROOT.TF1("fit6","pol0(1)",5.09e3,4e4)
        fit4=ROOT.TF1("SuperPosition", "[0]*TMath::Landau(x,[1],[2])+pol0(3)",5.09e3,4e4) ##((mu2*2-std2)/3),4e4 ##pol0 + expo
        fit4.SetParNames("Amplitude", "Mean", "Sigma", "pol_0")
        fit4.SetParameters(300, 5500, 90, 6) 
        project.Fit(fit4, "R+")
        
        fit5.SetParameters(fit4.GetParameters()[0],fit4.GetParameters()[1],fit4.GetParameters()[2])
        fit6.SetParameters(fit4.GetParameters()[3],fit4.GetParameters()[3])
        fit5.SetLineColor(1)
        fit5.SetLineStyle(5)
        fit6.SetLineColor(kGreen+2) 
        fit6.SetLineStyle(4)
        
        fit5.Draw("same")
        fit6.Draw("same")
        
        cutValue = 1.25e4
        #get number of good events
        xaxis = project.GetXaxis()
        binx = xaxis.FindBin(cutValue)
        goodEvents = project.Integral(1,binx)
        print("good events: " + str(goodEvents))
        
        #get total number of events
        bintotal = xaxis.GetNbins()
        allEvents = project.Integral(1,bintotal)
        print("all events: " + str(allEvents))    
        
        #percentage
        perc = goodEvents/allEvents
        goodEventsPercent.append(perc)
        recoilEn = (lbin[i] + ubin[i])/2
        recoilEnergy.append(recoilEn)
        
        #cv = 4.65e3
        #
        #
        #
        #binmax  = project.GetMaximumBin()
        #print("Maximum bin ... " + str(binmax))
        #print("bin number **** " + str(binx) + " ----- " + str(project.GetBinContent(binmax-2)))
        
        chiSqVals.append(cutValue)
        chiSqVals2=np.append(chiSqVals2,cutValue)
        norm1,mu1,std1=fit4.GetParameter(0),fit4.GetParameter(1),fit4.GetParameter(2)
        ermu1,erstd1=fit4.GetParError(1),fit4.GetParError(2) 
        mu,std=np.append(mu,mu1),np.append(std,std1)
        ermu,erstd=np.append(ermu,ermu1),np.append(erstd,erstd1)        
    if i == 3:
        fit5=ROOT.TF1("fit5","[0]*TMath::Landau(x,[1],[2])",7.09e3,4e4)
        fit6=ROOT.TF1("fit6","pol0(1)",7.09e3,4e4)
        fit4=ROOT.TF1("SuperPosition", "[0]*TMath::Landau(x,[1],[2])+pol0(3)",7.09e3,4e4) ##((mu2*2-std2)/3),4e4 ##pol0 + expo
        fit4.SetParNames("Amplitude", "Mean", "Sigma", "pol_0")
        fit4.SetParameters(300, 7000, 120, 6) 
        project.Fit(fit4, "R+")
        
        fit5.SetParameters(fit4.GetParameters()[0],fit4.GetParameters()[1],fit4.GetParameters()[2])
        fit6.SetParameters(fit4.GetParameters()[3],fit4.GetParameters()[3])
        fit5.SetLineColor(1)
        fit5.SetLineStyle(5)
        fit6.SetLineColor(kGreen+2) 
        fit6.SetLineStyle(4)
        
        fit5.Draw("same")
        fit6.Draw("same")
        
        cutValue = 1.48e4
        #get number of good events
        xaxis = project.GetXaxis()
        binx = xaxis.FindBin(cutValue)
        goodEvents = project.Integral(1,binx)
        print("good events: " + str(goodEvents))
        
        #get total number of events
        bintotal = xaxis.GetNbins()
        allEvents = project.Integral(1,bintotal)
        print("all events: " + str(allEvents))  
        
        #percentage
        perc = goodEvents/allEvents
        goodEventsPercent.append(perc)
        recoilEn = (lbin[i] + ubin[i])/2
        recoilEnergy.append(recoilEn)        
        
        chiSqVals.append(cutValue)
        chiSqVals2=np.append(chiSqVals2,cutValue)
        norm1,mu1,std1=fit4.GetParameter(0),fit4.GetParameter(1),fit4.GetParameter(2)
        ermu1,erstd1=fit4.GetParError(1),fit4.GetParError(2)
        mu,std=np.append(mu,mu1),np.append(std,std1)
        ermu,erstd=np.append(ermu,ermu1),np.append(erstd,erstd1)        
    if i == 4:
        fit5=ROOT.TF1("fit5","[0]*TMath::Landau(x,[1],[2])",9.5e3,4e4)
        fit6=ROOT.TF1("fit6","pol0(1)",9.5e3,4e4)
        fit4=ROOT.TF1("SuperPosition", "[0]*TMath::Landau(x,[1],[2])+pol0(3)",9.5e3,4e4) ##((mu2*2-std2)/3),4e4 ##pol0 + expo
        fit4.SetParNames("Amplitude", "Mean", "Sigma", "pol_0")
        fit4.SetParameters(250, 10000, 150, 6) 
        project.Fit(fit4, "R+")
        
        fit5.SetParameters(fit4.GetParameters()[0],fit4.GetParameters()[1],fit4.GetParameters()[2])
        fit6.SetParameters(fit4.GetParameters()[3],fit4.GetParameters()[3])
        fit5.SetLineColor(1)
        fit5.SetLineStyle(5)
        fit6.SetLineColor(kGreen+2) 
        fit6.SetLineStyle(4)
        
        fit5.Draw("same")
        fit6.Draw("same")
        
        cutValue = 1.789e4
        #get number of good events
        xaxis = project.GetXaxis()
        binx = xaxis.FindBin(cutValue)
        goodEvents = project.Integral(1,binx)
        print("good events: " + str(goodEvents))
        
        #get total number of events
        bintotal = xaxis.GetNbins()
        allEvents = project.Integral(1,bintotal)
        print("all events: " + str(allEvents))  
        
        #percentage
        perc = goodEvents/allEvents
        goodEventsPercent.append(perc)
        recoilEn = (lbin[i] + ubin[i])/2
        recoilEnergy.append(recoilEn)        
        
        chiSqVals.append(cutValue)
        chiSqVals2=np.append(chiSqVals2,cutValue)
        norm1,mu1,std1=fit4.GetParameter(0),fit4.GetParameter(1),fit4.GetParameter(2)
        ermu1,erstd1=fit4.GetParError(1),fit4.GetParError(2)
        mu,std=np.append(mu,mu1),np.append(std,std1)
        ermu,erstd=np.append(ermu,ermu1),np.append(erstd,erstd1)        
    if i == 5:
        fit5=ROOT.TF1("fit5","[0]*TMath::Landau(x,[1],[2])",12.18e3,4e4)
        fit6=ROOT.TF1("fit6","pol0(1)",12.18e3,4e4)
        fit4=ROOT.TF1("SuperPosition", "[0]*TMath::Landau(x,[1],[2])+pol0(3)",12.18e3,4e4) ##((mu2*2-std2)/3),4e4 ##pol0 + expo
        fit4.SetParNames("Amplitude", "Mean", "Sigma", "pol_0")
        fit4.SetParameters(200, 12000, 175, 6) 
        project.Fit(fit4, "R+")
        
        fit5.SetParameters(fit4.GetParameters()[0],fit4.GetParameters()[1],fit4.GetParameters()[2])
        fit6.SetParameters(fit4.GetParameters()[3],fit4.GetParameters()[3])
        fit5.SetLineColor(1)
        fit5.SetLineStyle(5)
        fit6.SetLineColor(kGreen+2) 
        fit6.SetLineStyle(4)
        
        fit5.Draw("same")
        fit6.Draw("same")
        
        cutValue = 2.31e4
        #get number of good events
        xaxis = project.GetXaxis()
        binx = xaxis.FindBin(cutValue)
        goodEvents = project.Integral(1,binx)
        print("good events: " + str(goodEvents))
        
        #get total number of events
        bintotal = xaxis.GetNbins()
        allEvents = project.Integral(1,bintotal)
        print("all events: " + str(allEvents))   
        
        #percentage
        perc = goodEvents/allEvents
        goodEventsPercent.append(perc)
        recoilEn = (lbin[i] + ubin[i])/2
        recoilEnergy.append(recoilEn)        
        
        chiSqVals.append(cutValue)
        chiSqVals2=np.append(chiSqVals2,cutValue)
        norm1,mu1,std1=fit4.GetParameter(0),fit4.GetParameter(1),fit4.GetParameter(2)
        ermu1,erstd1=fit4.GetParError(1),fit4.GetParError(2)
        mu,std=np.append(mu,mu1),np.append(std,std1)
        ermu,erstd=np.append(ermu,ermu1),np.append(erstd,erstd1)        
    if i == 6:
        fit5=ROOT.TF1("fit5","[0]*TMath::Landau(x,[1],[2])",15.8e3,4e4)
        fit6=ROOT.TF1("fit6","pol0(1)",15.8e3,4e4)
        fit4=ROOT.TF1("SuperPosition", "[0]*TMath::Landau(x,[1],[2])+pol0(3)",15.8e3,4e4) ##((mu2*2-std2)/3),4e4 ##pol0 + expo
        fit4.SetParNames("Amplitude", "Mean", "Sigma", "pol_0")
        fit4.SetParameters(100, 16000, 195, 6) 
        project.Fit(fit4, "R+")
        
        fit5.SetParameters(fit4.GetParameters()[0],fit4.GetParameters()[1],fit4.GetParameters()[2])
        fit6.SetParameters(fit4.GetParameters()[3],fit4.GetParameters()[3])
        fit5.SetLineColor(1)
        fit5.SetLineStyle(5)
        fit6.SetLineColor(kGreen+2) 
        fit6.SetLineStyle(4)
        
        fit5.Draw("same")
        fit6.Draw("same")
        
        cutValue = 2.6e4
        #get number of good events
        xaxis = project.GetXaxis()
        binx = xaxis.FindBin(cutValue)
        goodEvents = project.Integral(1,binx)
        print("good events: " + str(goodEvents))
        
        #get total number of events
        bintotal = xaxis.GetNbins()
        allEvents = project.Integral(1,bintotal)
        print("all events: " + str(allEvents))   
        
        #percentage
        perc = goodEvents/allEvents
        goodEventsPercent.append(perc)
        recoilEn = (lbin[i] + ubin[i])/2
        recoilEnergy.append(recoilEn)        
        
        chiSqVals.append(cutValue)
        chiSqVals2=np.append(chiSqVals2,cutValue)
        norm1,mu1,std1=fit4.GetParameter(0),fit4.GetParameter(1),fit4.GetParameter(2)
        ermu1,erstd1=fit4.GetParError(1),fit4.GetParError(2)
        mu,std=np.append(mu,mu1),np.append(std,std1)
        ermu,erstd=np.append(ermu,ermu1),np.append(erstd,erstd1)        
    if i == 7:
        fit5=ROOT.TF1("fit5","[0]*TMath::Landau(x,[1],[2])",18.09e3,4e4)
        fit6=ROOT.TF1("fit6","pol0(1)",18.09e3,4e4)
        fit4=ROOT.TF1("SuperPosition", "[0]*TMath::Landau(x,[1],[2])+pol0(3)",18.09e3,4e4) ##((mu2*2-std2)/3),4e4 ##pol0 + expo
        fit4.SetParNames("Amplitude", "Mean", "Sigma", "pol_0")
        fit4.SetParameters(50, 18000, 200, 6) 
        project.Fit(fit4, "R+")
        
        fit5.SetParameters(fit4.GetParameters()[0],fit4.GetParameters()[1],fit4.GetParameters()[2])
        fit6.SetParameters(fit4.GetParameters()[3],fit4.GetParameters()[3])
        fit5.SetLineColor(1)
        fit5.SetLineStyle(5)
        fit6.SetLineColor(kGreen+2) 
        fit6.SetLineStyle(4)
        
        fit5.Draw("same")
        fit6.Draw("same")
        
        cutValue = 3.45e4
        #get number of good events
        xaxis = project.GetXaxis()
        binx = xaxis.FindBin(cutValue)
        goodEvents = project.Integral(1,binx)
        print("good events: " + str(goodEvents))
        
        #get total number of events
        bintotal = xaxis.GetNbins()
        allEvents = project.Integral(1,bintotal)
        print("all events: " + str(allEvents))   
        
        #percentage
        perc = goodEvents/allEvents
        goodEventsPercent.append(perc)
        recoilEn = (lbin[i] + ubin[i])/2
        recoilEnergy.append(recoilEn)        
        
        chiSqVals.append(cutValue)
        chiSqVals2=np.append(chiSqVals2,cutValue)
        norm1,mu1,std1=fit4.GetParameter(0),fit4.GetParameter(1),fit4.GetParameter(2)
        ermu1,erstd1=fit4.GetParError(1),fit4.GetParError(2)
        mu,std=np.append(mu,mu1),np.append(std,std1)
        ermu,erstd=np.append(ermu,ermu1),np.append(erstd,erstd1)  
        
    #draw the cut line    
    chisq_cut=ROOT.TLine(cutValue,C2.GetUymin(),cutValue,C2.GetUymax()) 
    chisq_cut.SetLineColor(kBlack)
    chisq_cut.SetLineWidth(2)
    chisq_cut.SetLineStyle(3)
    chisq_cut.Draw("same")
    
    ROOT.gStyle.SetOptFit(1)
    C2.SaveAs("charge_chisq_s1/project_Qchisq_%d_%d.gif"%(lbin[i],ubin[i]))



gamma1=ROOT.TLine(80,0,80,40000)
gamma2=ROOT.TLine(119,0,119,40000)

fitfunc3=ROOT.TF1("fitfunc3","pol2",10,2000)
fitfuncmean=ROOT.TF1("fitfuncmean","pol2",10,2000)
fitchisq=ROOT.TF1("fitfuncmean","pol2",10,2000)

fitfuncmean.SetLineColor(kBlack)
fitfunc3.SetLineColor(kRed)
fitchisq.SetLineColor(kRed)
fitfuncmean.SetLineStyle(2)
fitfunc3.SetLineStyle(2)

n=np.size(bincent)
error3=np.sqrt(ermu**2+9*erstd**2)
zeros=np.zeros(len(ermu))

print(chiSqVals2)

Qchisq.cd()
hist.Draw("colz")
mean=ROOT.TGraph(n,bincent,mu)
mean.Fit(fitfuncmean,"IREM+")
mean.SetLineStyle(kDashed)
mean.SetMarkerColor(kOrange+2)
mean.SetMarkerStyle(8)
mean.SetMarkerSize(.5)
mean.Draw("same P")

m3=ROOT.TGraphErrors(n,bincent,mu+3*std,zeros,error3) ##mu+3*std
m3.Fit(fitfunc3,"IREM+")
m3.SetLineColor(kRed)
m3.SetLineStyle(kDashed)
m3.SetMarkerColor(kOrange+2)
m3.SetMarkerStyle(8)
m3.SetMarkerSize(.5)
m3.SetTitle("Fitting with pol2 for 3 #sigma lower band for AmBe_izip;bincent in qsum1 (keV); #mu + 3#sigma in Qchisq")
m3.Draw("same P")

#chisq=ROOT.TGraphErrors(n,bincent,chiSqVals-3*std,zeros,error3) ##mu+3*std
chisq=ROOT.TGraph(n,bincent,chiSqVals2)
chisq.Fit(fitchisq,"IREM+")
chisq.SetLineColor(kRed)
#chisq.SetMarkerColor(kOrange+2)
#chisq.SetMarkerStyle(8)
#chisq.SetMarkerSize(.8)
#chisq.SetTitle("Fitting with pol2 for 3 #sigma lower band for AmBe_izip;bincent in qsum1 (keV); #mu + 3#sigma in Qchisq")
chisq.Draw("same P")

Qchisq.SaveAs("charge_chisq_s1/charge chisq cut for AmBe.gif")

plt.plot(recoilEnergy, goodEventsPercent, 'ro-')
plt.grid("on")
plt.title("Efficiency vs Recoil Energy",fontsize=24)
plt.xlabel("Recoil Energy (keV)",fontsize=18)
plt.ylabel("Efficiency", fontsize=18)
plt.xlim([0,350])
#plt.ylim([0,1.0])
#plt.show()


