import sys
import pandas as pd
import json
import math
import random
import plotly.express as px

df = pd.read_csv('data/2018_NYPD_Data.csv', low_memory=False)
precinct_pop_df = pd.read_csv('data/precinct_populations.csv')

crime_counts = df['ADDR_PCT_CD'].value_counts().to_dict()
nycmap = json.load(open('data/geojsons/Police Precincts.geojson'))

mapdata = nycmap['features']
d = []
for x in mapdata:
    precinct = float(x['properties']['precinct'])
    pop = precinct_pop_df['P0010001'].where(precinct_pop_df['precinct_2020'] == int(precinct)).dropna().values[0]
    n_crimes = crime_counts[precinct]
    crime_rate = n_crimes / pop * 100000
    d.append([precinct, pop, n_crimes, crime_rate])


df = pd.DataFrame(d, columns=['precinct', 'population', 'n_crimes', 'crime_rate'])
df = df[df.precinct != 22]
df = df[df.precinct != 14]
print(df)

fig = px.choropleth_mapbox(df,
                           geojson=nycmap,
                           locations='precinct',
                           featureidkey='properties.precinct',
                           color='crime_rate',
                           color_continuous_scale='viridis',
                           mapbox_style='carto-positron',
                           zoom=9, center={'lat': 40.7, 'lon': -73.9},
                           opacity=0.7,
                           hover_name='precinct'
                           )

fig.show()

