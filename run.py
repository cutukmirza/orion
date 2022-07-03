from dash import Dash,callback, Output, Input
import dash_bootstrap_components as dbc
from flask_migrate import Migrate


from app.layouts.base import base_layout
from app.layouts.home import home_layout
from app.layouts.invoice import invoice_layout
from app.layouts.members import member_layout
from app.layouts.alumni import alumni_layout
from flask import Flask
import config
from app.models.db.shared  import db
from app.models.db.shared  import server

from app.models.db.member import Member


def create_app(test_config=None):

    FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
    

    app = Dash(__name__, suppress_callback_exceptions=True, 
    external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME],
    server=server)

    server.config.from_object(config.DevelopmentConfig)

    
    app.title = "Orion"
    #app._favicon = "images/favicon.png"

    # CORS(app)
    db.init_app(server)
    migrate = Migrate(app, db)

    with server.app_context():
        # app.layout = html.Div(children=[
        #     html.H1(children='Hello Dash'),

        #     html.Div(children='''
        #         Dash: A web application framework for your data.
        #     '''),
        #     html.Div(
        #         str(Patient.read_all()[:3])
        #     )
        # ])
        app.layout = base_layout

    return app

# Update the index
@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home_layout
    elif pathname == '/invoice':
        return invoice_layout
    elif pathname == '/members':
        return member_layout
    elif pathname == '/alumni':
        return alumni_layout    
    else:
        return home_layout
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app = create_app()
    app.run_server(debug=True)


