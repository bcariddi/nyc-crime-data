import pandas as pd
import json
import math
import random
import plotly.express as px
from area import area

nycmap = json.load(open('data/precinct-boundaries/Police Precincts.geojson'))

mapdata = nycmap['features']
d = []
for x in mapdata:
    precinct = int(x['properties']['precinct'])
    n_crimes = random.randint(1, 100)
    d.append([precinct, n_crimes])


df = pd.DataFrame(d, columns=['precinct', 'n_crimes'])
print(df)

fig = px.choropleth_mapbox(df,
                           geojson=nycmap,
                           locations='precinct',
                           featureidkey='properties.precinct',
                           color='n_crimes',
                           color_continuous_scale='viridis',
                           mapbox_style='carto-positron',
                           zoom=9, center={'lat': 40.7, 'lon': -73.9},
                           opacity=0.7,
                           hover_name='precinct'
                           )

fig.show()
