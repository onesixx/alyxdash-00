import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_admin_components as dac
#from pages.basic_boxes.model import plot_scatter
#from .model import plot_scatter

import plotly.graph_objs as go
import numpy as np
import pandas as pd


def plot_scatter(N=50):

    trace1 = go.Scatter(
        y=np.random.randn(N),
        mode='markers',
        marker=dict(
            size=16,
            color=np.random.randn(N),  # set color equal to a variable
            colorscale='Viridis',
            showscale=True
        )
    )
    return dict(data=[trace1])


content = dac.TabItem(id='content_basic_boxes',
                      children=html.Div(
                          [
                              dac.SimpleBox(
                                  title="Box 1",
                                  children=[
                                      dcc.Graph(
                                          id='box-graph',
                                          config=dict(displayModeBar=False),
                                          style={'width': '100%'}
                                      )
                                  ],
                                  style={'height': "600px"},
                              ),
                              dac.SimpleBox(
                                  style={'height': "600px"},
                                  title="Box 2",
                                  children=[
                                      dcc.Graph(
                                          figure=plot_scatter(),
                                          config=dict(displayModeBar=False),
                                          style={'width': '100%'}
                                      )
                                  ]
                              )
                          ],
                          className='row'
                      )
                      )
