import numpy as np
import matplotlib.pyplot as plt



def RMSE(M,S):
    # M Measured
    # S Simulater or calculated
    # Estimates the sum of the differences
    E=0
    for m,s in zip(M,S):
        E=E+(m-s)**2
    # Estimates root squate and averages it
    E=E**(1/2)
    E=E/len(M)
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

def Error1(M=np.array([]),S=np.array([])):
    E=RMSE(M,S)
    PlotError(M,S)
    PlotValue("RMSE="+str(E))