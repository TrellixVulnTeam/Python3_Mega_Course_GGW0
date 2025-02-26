from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_Time"] = df["Start Time"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_Time"] = df["End Time"].dt.strftime("%Y-%m-%d %H:%M:%S")


cds = ColumnDataSource(df)


p = figure(x_axis_type="datetime", height=200,width=800,title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1


hover = HoverTool(tooltips=[("Start","@Start_Time"),("End","@End_Time")])
p.add_tools(hover)

q = p.quad(left="Start Time",right="End Time",bottom=0,top=1, color="green", source=cds)

output_file("Graph.html")
show(p)