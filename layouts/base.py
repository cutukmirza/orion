# External
from dash import html, dcc
import dash_bootstrap_components as dbc

# Internal
from elements.sidebar import sidebar


CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

base_layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    html.Div(id="page-content", style=CONTENT_STYLE)
])