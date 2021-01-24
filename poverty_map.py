import sys
import pandas as pd
import json
import math
import random
import plotly.express as px

df = pd.read_csv('data/Poverty.csv')
df = df[df['TimeFrame'] == 2018]
df['Fips'] = pd.to_numeric(df['Fips'], errors='coerce')

district_pop_df = pd.read_csv('data/district_populations.csv')
district_pop_df = district_pop_df[district_pop_df['TimeFrame'] == 2018]
district_pop_df['Fips'] = pd.to_numeric(district_pop_df['Fips'], errors='coerce')

nycmap = json.load(open('data/geojsons/Community Districts.geojson'))

mapdata = nycmap['features']
d = []
for x in mapdata:
    district = float(x['properties']['boro_cd'])
    try:
        pop = district_pop_df['Data'].where(district_pop_df['Fips'] == int(district)).dropna().values[0]
        n_pov = df['Data'].where(df['Fips'] == int(district)).dropna().values[0]
        pov_rate = n_pov / pop * 100000
        d.append([district, pop, n_pov, pov_rate])
    except:
        print(str(district) + ' missing data')


df = pd.DataFrame(d, columns=['district', 'population', 'n_pov', 'pov_rate'])
print(df)

fig = px.choropleth_mapbox(df,
                           geojson=nycmap,
                           locations='district',
                           featureidkey='properties.boro_cd',
                           color='pov_rate',
                           color_continuous_scale='viridis',
                           mapbox_style='carto-positron',
                           zoom=9, center={'lat': 40.7, 'lon': -73.9},
                           opacity=0.7,
                           hover_name='district'
                           )

fig.show()
fig.write_html('poverty_map.html')
