import sys
import pandas as pd
import json
import math
import random
import plotly.graph_objects as go

df = pd.read_csv('data/seven-major-felony-offenses-2000-2019.csv')
print(df)

years = [*range(2000, 2020)]
print(years)

df_list = df.values.tolist()
print(df_list)

fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=df_list[0][1:], name='Murder & Manslaughter', line=dict(color='red', width=4)))
fig.add_trace(go.Scatter(x=years, y=df_list[1][1:], name='Rape', line=dict(color='orange', width=4)))
fig.add_trace(go.Scatter(x=years, y=df_list[2][1:], name='Robbery', line=dict(color='green', width=4)))
fig.add_trace(go.Scatter(x=years, y=df_list[3][1:], name='Felony Assault', line=dict(color='blue', width=4)))
fig.add_trace(go.Scatter(x=years, y=df_list[4][1:], name='Burglary', line=dict(color='black', width=4)))
fig.add_trace(go.Scatter(x=years, y=df_list[5][1:], name='Grand Larceny', line=dict(color='brown', width=4)))
fig.add_trace(go.Scatter(x=years, y=df_list[6][1:], name='Grand Larceny of Motor Vehicle', line=dict(color='grey', width=4)))

fig.update_yaxes(type="log")


fig.update_layout(title='Seven Major Felonies in NYC',
                  xaxis_title='Year',
                  yaxis_title='Number of crimes reported')

fig.write_html('seven_major.html')
