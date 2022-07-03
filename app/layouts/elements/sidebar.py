"""
dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
# External
import dash_bootstrap_components as dbc
from dash import html, dcc
# Internal
from app.img import img

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.Img(width='100%', src="data:image/png;base64,{}".format(img.iaeste_logo_blue.decode())),
        #html.H2("IAESTE Switzerland", className="display-5"),
        html.Hr(),
        html.P(
            "A simple management system", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink('Home', href='/home', active="exact"),
                dbc.NavLink('Invoice', href='/invoice', active="exact"),
                dbc.NavLink('Members', href='/members', active="exact"),
                dbc.NavLink('Alumni', href='/alumni', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

