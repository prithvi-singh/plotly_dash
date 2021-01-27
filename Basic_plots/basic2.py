# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:35:43 2021

@author: Prithvi Raj Singh
"""

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as  pd

# Read data
df = pd.read_csv('Data/2018WinterOlympics.csv')


# Basic bar chart
data = [go.Bar(x=df['NOC'], y=df['Total'])]
layout = go.Layout(title='Medals')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

# Nested bar chart

trace1 = go.Bar(x=df['NOC'], y=df['Gold'],
                name='Gold', marker={'color':'#FFD700'})
trace2 = go.Bar(x=df['NOC'], y=df['Silver'],
                name='Silver', marker={'color':'#9EA0A1'})
trace3 = go.Bar(x=df['NOC'], y=df['Bronze'],
                name='Bronze', marker={'color':'#CD7F32'})

data = [trace1, trace2, trace3]
layout = go.Layout(title='Medals')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

# Stacked bar chart- just add barmode='stack in layout

layout = go.Layout(title='Medals', barmode='stack')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)


