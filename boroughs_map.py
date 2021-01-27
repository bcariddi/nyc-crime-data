import sys
import pandas as pd
import json
import math
import random
import plotly.express as px

df = pd.read_csv('data/2018_NYPD_Data.csv', low_memory=False)

crime_counts = df['BORO_NM'].value_counts().to_dict()
print(crime_counts)
nycmap = json.load(open('data/geojsons/boroughs.geojson'))

mapdata = nycmap['features']
d = []
for x in mapdata:
    borough = x['properties']['boro_name'].upper()
    n_crimes = crime_counts[borough]
    d.append([borough, n_crimes])

df = pd.DataFrame(d, columns=['borough', 'n_crimes'])

fig = px.choropleth_mapbox(df,
                           geojson=nycmap,
                           locations='borough',
                           featureidkey='properties.boro_nm',
                           color='n_crimes',
                           color_continuous_scale='viridis',
                           mapbox_style='carto-positron',
                           zoom=9, center={'lat': 40.7, 'lon': -73.9},
                           opacity=0.7,
                           hover_name='borough'
                           )

fig.show()
