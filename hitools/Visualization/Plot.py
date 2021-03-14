from bokeh.models import ColumnDataSource
from bokeh.plotting import figure,show
from bokeh.io import output_notebook, push_notebook, show
import numpy as np


class ViewData:
    def __init__(self, x=np.linspace(1,100,100),y=np.sin(x),*y2=y=np.sin(x) ,output=0,Title="Data visualization"):
        """ instatiating the object view data

        Args:
            x ([type], numpy): [description]. Defaults to np.linspace(1,100,100).
            y ([type], numpy): [description]. Defaults to np.sin(x).
            y2 ([type], numpy): [description]. Defaults to np.sin(x).
            output = 1 a integer that refer to use in a notebook or using 0 refers to creating html file
            Title (str, optional): [description]. Defaults to "Data visualization".
        """
        # create a new plot with a title and axis labels
        data={'x':x,'y':y,'y2':y2}
        self.source=ColumnDataSource(data=data)
        self.fig = figure(title=Title, x_axis_label='x', y_axis_label='y',plot_width=300,plot_height=300)
        if output =0:
            output_file()
        else:
            output_notebook()






    def xy(self,Lab="Serie 1"):
        self.fig.line(x=x, y=y, legend_label=Lab, line_width=2,source=self.fig.source)
        try:
            output_notebook()
        show(self.fig)
