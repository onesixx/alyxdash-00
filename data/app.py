from dash import Dash
import dash_admin_components as dac

import alyxdash 
#from frontend.mainboard.view import navbar, sidebar, body, controlbar, footer
from alyxdash.templates  import layout
import pages
# =============================================================================
# Dash App and Flask Server
# =============================================================================
app_dash = Dash(__name__)
server = app_dash.server

# =============================================================================
# App Layout
# =============================================================================
#app_dash.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
app_dash.layout = layout
# =============================================================================
# Callback
# =============================================================================
alyxdash.callbacks.get_callbacks(app_dash)

pages.tab_cards.callbacks.get_callbacks(app_dash)
pages.basic_boxes.callbacks.get_callbacks(app_dash)
pages.gallery_1.callbacks.get_callbacks(app_dash)
pages.gallery_2.callbacks.get_callbacks(app_dash)

# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app_dash.run_server(debug=False)
