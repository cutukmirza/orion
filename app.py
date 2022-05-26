from email.mime import base
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from layouts.base import base_layout
from layouts.home import home_layout
from layouts.invoice import invoice_layout

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME])

app.layout = base_layout

# Update the index
@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home_layout
    elif pathname == '/invoice':
        return invoice_layout
    else:
        return home_layout
    # You could also return a 404 "URL not found" page here

if __name__ == '__main__':
    app.run_server(debug=True)