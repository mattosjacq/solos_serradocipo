# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:27:51 2017

@author: matto
"""

import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='jacqmattos', api_key='wPca1ZaG5qRhYwUm1MfX')
import pandas as pd



df = pd.read_excel(r'C:\Jac\Mestrado\Projeto\Campo\Variaveis_Cipo_Jacque.xlsx')
df.head()

###definir as colunas que vao ser usadas
#df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

data = [ dict(
        type = 'scattergeo',
        locationmode = 'country names',
        lon = df['lon'],
        lat = df['lat'],
        #text = df['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = scl,
            cmin = 0,
            color = df['Areia_Grossa'],
            cmax = df['Areia_Grossa'].max(),
            colorbar=dict(
                title="Proporção de Areia"
            )
        ))]
            

layout = dict(
        title = 'Solos da Serra do Cipó',
        colorbar = True,
        geo = dict(
            scope='brazil',
            #domain=([-44.0,-43.0],[-20.0, -19.0]),
            #lonaxis = dict( range= [ -44.0, -43.0 ] ),
            #lataxis = dict( range= [ -20.0, -19.0 ] ),
            #projection=dict( type='merc' ),
            projection = dict(
            type = 'Mercator'
            ),
            lonaxis = dict( range= [ -43.7,-43.4 ] ),
            lataxis = dict( range= [ -19.40, -19.20 ] ),
            domain = ([-43.7,-43.4],[-19.40, -19.20]),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )
            

fig = dict( data=data, layout=layout )
py.iplot(fig, validate=False, filename='solos' )