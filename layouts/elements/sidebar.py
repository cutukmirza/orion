"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash_bootstrap_components as dbc
from dash import html, dcc


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

# the styles for the main content position it to the right of the sidebar and
# add some padding.

sidebar = html.Div(
    [
        html.H2("IAESTE Switzerland", className="display-5"),
        html.Hr(),
        html.P(
            "A simple management system", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink('Home', href='/home', active="exact"),
                dbc.NavLink('Invoice', href='/invoice', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

