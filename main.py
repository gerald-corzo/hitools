from hitools.Visualization.Hydrograph import Basic
import numpy as np


x=np.linspace(1,100,100)
y=np.sin(x/15)
y2=np.cos(x/15)

Basic(x,y,y2)


