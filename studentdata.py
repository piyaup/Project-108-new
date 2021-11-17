import csv
import plotly.figure_factory as ff
import pandas as pd 

df = pd.read_csv("studentdata.csv")
fig = ff.create_distplot([df["AvgRating"].tolist()],["AvgRating"],show_hist = True)
fig.show()