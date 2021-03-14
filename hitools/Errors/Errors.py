import numpy as np
import matplotlib.pyplot as plt


def RMSE(T,S):
    # S Simulater or calculated
    # T Measured
    E=0
    # Estimates the sum of the differences
    E=(T-S)**2
    E=np.nansum(E)
    
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
    E=(T-S)**2
    E=np.nansum(E)
    E=E/len(T)
    return E    

def PlotError(M,S):
    figure, axes=plt.subplots(nrows=2,ncols=1)
    plt.subplot(2,1,1)
    plt.plot(M)
    plt.plot(S)
    plt.ylabel("Value of the time series")
    plt.subplot(2,1,2)
    plt.title("Error (Measured - Simulated)")
    plt.plot(M-S)
    plt.xlabel("Time series (h)")
    plt.ylabel("Error")
    figure.tight_layout(pad=3.0)
    


def PlotValue(Mytext):
    plt.figure()
    plt.axis('off')
    plt.text(0.6, 0.7, Mytext, size=50, rotation=0.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )


    

def Error1(T=np.array([]),S=np.array([])):
    Temp=RMSE(T,S)
    R={"RMSE":Temp , "sd_T":np.std(T),"MSE":MSE(T,S), "sd_S":np.std(S), 
    "NRMSE":Temp/np.std(T),
    "Nash": 1-np.nansum((T-S)**2)/np.nansum((T-np.nanmean(T))**2),
    "Cor":np.nansum((S-np.nanmean(S))*(T-np.nanmean(T)))/(np.sqrt(np.nansum((S-np.nanmean(S))**2))*np.sqrt(np.nansum((T-np.nanmean(T))**2)))
    }
    PlotError(T,S)
    PlotValue("RMSE="+str(R["RMSE"]))
    return R
    