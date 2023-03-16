import numpy as np
import pandas as pd
import plotly.graph_objs as go


def make_data(N):
    data = np.random.randn(N)
    return data

data = make_data(N=50)


# def plot_scatter(N=50):
#     trace1 = go.Scatter(
#         y=data,
#         mode='markers',
#         marker=dict(
#             size=16,
#             color=np.random.randn(N),  # set color equal to a variable
#             colorscale='Viridis',
#             showscale=True
#         )
#     )
#     return dict(data=[trace1])
