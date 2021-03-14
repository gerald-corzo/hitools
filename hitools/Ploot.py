from bokeh.plotting import figure,show
from bokeh.io import output_notebook, push_notebook, show



class ViewData:

    def __init__(self, x=[1,2,3],*y=[1, 15,30],Title="Data visualization"):
        # create a new plot with a title and axis labels
        self.x=x
        self.y=y
        self.fig = figure(title=Title, x_axis_label='x', y_axis_label='y')

    def xy(self,Lab="Serie 1"):
        for i in self.y:
            self.fig.line(self.x, i, legend_label=Lab, line_width=2)
        try:
            output_notebook()
        show(self.fig)
