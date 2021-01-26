# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:11:41 2021

@author: Prithvi Raj Singh
"""

import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

# Scatter Plot
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_x, 
                   y=random_y, 
                   mode='markers',
                   marker=dict(
                       size=12,
                       color='rgb(51,204,153)',
                       symbol='pentagon',
                       line={'width':2}
                       ))]

layout = go.Layout(title='Hello First Plot',
                   xaxis={'title':'MY X AXIS'},
                   yaxis=dict(title='MY Y AXIS'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='scatter.html')

# Line Charts

x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

trace0 = go.Scatter(x=x_values, y=y_values+5,
                   mode='markers', name='markers')
trace1 = go.Scatter(x=x_values, y=y_values,
                    mode='lines', name='mylines')
trace2 = go.Scatter(x=x_values, y=y_values-5,
                    mode='lines+markers', name='my favorite')

data = [trace0, trace1, trace2]

layout = go.Layout(title='Line Charts')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)

# Plots with actual data

df = pd.read_csv('SourceData/nst-est2017-alldata.csv')

df2 = df[df['DIVISION']=='1']
df2.set_index('NAME', inplace=True)

list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_col]

data = [go.Scatter(x=df.columns,
                   y=df2.loc[name], 
                   mode='lines', 
                   name=name) for name in df2.index]

pyo.plot(data)