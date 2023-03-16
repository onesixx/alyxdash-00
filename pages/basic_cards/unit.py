from dash import Dash, dcc, html
import dash_admin_components as dac
import plotly.graph_objs as go


def plot_pie():
    labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
    values = [4500, 2500, 1053, 500]
    colors = ['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']
    trace = go.Pie(
        labels=labels, values=values,
        hoverinfo='label+percent', textinfo='value',
        textfont=dict(size=20),
        marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    return dict(data=[trace])


view = dcc.Graph(
    figure=plot_pie(),
    config=dict(
        displayModeBar=False
    ),
    style={'width': '100%'}
)

# =============================================================================
# Dash App and Flask Server
# =============================================================================
app_dash = Dash(__name__)
# =============================================================================
# App Layout
# =============================================================================
#app_dash.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
app_dash.layout = view
# =============================================================================
# Callback
# =============================================================================
# frontend.pages.tab_cards.callbacks.get_callbacks(app_dash)

# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app_dash.run_server(debug=False)
