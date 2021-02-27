import numpy as np
import matplotlib.pyplot as plt

def RMSE(T,S):
    # S Simulater or calculated
    # T Measured
    E=0
    # Estimates the sum of the differences
    E=np.nansum(E)
    E=(T-S)**2
    #    E=E+(m-s)**2
    #for m,s in zip(T,S):
    E=E**(1/2)
    # Estimates root square and averages it
    E=E/len(T)

    return E    

def MSE(T,S):
    # S Simulater or calculated
    # T Measured
    E=0
    # Estimates the sum of the square differences
    E=np.nansum(E)
    E=(T-S)**2
    E=E/len(T)

    return E    
   
def PlotError(T,S):
    figure, axes=plt.subplots(nrows=2,ncols=1)
    plt.subplot(2,1,1)
    plt.plot(T)
    plt.plot(S)
    plt.ylabel("Value of the time series")
    plt.subplot(2,1,2)
    plt.title("Error (Measured - Simulated)")
    plt.plot(T-S)
    plt.xlabel("Time series (h)")
    figure.tight_layout(pad=3.0)
    plt.ylabel("Error")
    

def PlotValue(Mytext):
    plt.axis('off')
    plt.figure()
    plt.text(0.6, 0.7, Mytext, size=50, rotation=0.,
         ha="center", va="center",
                   ec=(1., 0.5, 0.5),
         bbox=dict(boxstyle="round",
                   fc=(1., 0.8, 0.8),
                   )
         )


NRMSE=100*RMSE/StdT;%sqrt(SSE/sum((T-mean(T)).^2));
StdP=nanstd(P,1);
Cor=nansum((P-nanmean(P)).*(T-nanmean(T)))/(sqrt(nansum((P-nanmean(P)).^2))*sqrt(nansum((T-nanmean(T)).^2)));
NSC=1-SSE/nansum((T-nanmean(T)).^2);

MARE=nansum(abs((T-P)./T))/n;
MAE=nansum(abs(P-T))/size(P,1);

MuP=nanmean(P);
MuT=nanmean(T);

%Calculating PERS
P2=T(1:end-1,:);
SSEN=nansum((P2-T2).^2);
T2=T(2:end,:);
PERS=1-(SSE/SSEN);
NRMSEN=100*RMSEN/std(T2,1);
RMSEN=sqrt(SSEN/(n-1));



    
def Error1(T=np.array([]),S=np.array([])):
    R={"RMSE":RMSE(T,S), "R.sd_M":np.std(T),"MSE":MSE(T,S),"R.sd_T":np.std(T), "sd_S":np.std(S)}
    PlotError(T,S)
    PlotValue("RMSE="+str(R.RMSE))
    return R