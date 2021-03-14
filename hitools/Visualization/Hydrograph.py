from bokeh.plotting import figure
from bokeh.models import LinearAxis, Range1d
import numpy as np
from bokeh.io import output_file, show

def Basic(x, Q, P, Text="My Hydroinformatics Title"):
    """
    Hydrograph [summary]
    This function will plot a hydrograph for the analysis of rainfall runoff relationships
    Parameters
    ----------
    x=time : [type] Numpy Array 
        [description] 
        Time series of time stamp
        Will contain values of the time step of each Q and P
    Q=Discharge : [type] Numpy Array
        [description]
        Will contain values of each Q or river discharge
    P=Precipitation : [type] Numpy Array
        [description]
        Will contain values of each Q or river discharge
    """   
    
    # P = Precipitation
    # Q is Discharge    
    # Seting the params for the first figure.
    s1 = figure(title=Text,x_axis_type="datetime",  plot_width=1000, plot_height=600)
    s1.title.text_font_size = '24pt'

    ymin = P.min()
    ymax = P.max()+0.5*P.max()
    # Setting the second y axis range name and range
    s1.extra_y_ranges = {"Precipitation": Range1d(start=ymax,end=ymin)}

    # Adding the second axis to the plot.  
    s1.add_layout(LinearAxis(y_range_name="Precipitation"), 'right')

    # Setting the rect glyph params for the first graph. 
    # Using the default y range and y axis here.           
    s1.line(x, Q)

    # Setting the rect glyph params for the second graph. 
    # Using the aditional y range named "foo" and "right" y axis here. 
    #s1.rect(x=x,y=P, width=0.3, height=0.1,color="red", y_range_name="Precipitation")
    s1.vbar(x=x,top=P, width=0.3,color="red", y_range_name="Precipitation")
    
    show(s1)
    #s1.y_range(1).flipped=True
    #s1.extra_y_ranges.flipped=True
    return s1
    