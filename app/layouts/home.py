from dash import html, dcc
import dash_bootstrap_components as dbc


import pdfkit
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import re


from app.models.db.member import User
from app.models.db.shared import server
from app.models.db.shared import db
import config

### Temporary solution
### Need to find a way to have 
### just one server and one db object
### That will be used everywhere
server.config.from_object(config.DevelopmentConfig)
db.init_app(server)
server.app_context().push()

user = User.read_one(1)
print(user)

env = Environment(
        loader = FileSystemLoader("assets/templates"),
        autoescape=select_autoescape()
    )

rendered_string = env.get_template('sig.html').render(
        name = user.name,
        email = user.email,
        phone = user.phone,
        committee = user.committee,
        )

print(rendered_string)

home_layout = html.Div(children=[
    html.H1(children='Hello Mirza'),

    html.Div(children=['''
        Welcome to your dashboard.
    ''',
    dbc.Row([
        dbc.Col(width=3, children=[
            dbc.Textarea(className="mb-3 mt-3", id="signature_textarea", value=rendered_string),
            dcc.Clipboard(
                target_id="signature_textarea",
                title="copy",
                style={
                    "display": "inline-block",
                    "fontSize": 20,
                    "verticalAlign": "top",
                },
            ),
            html.P(["Find instructions on how to install an HTML signature to your preferred email client ", 
            html.Span(html.A("here.", href="https://support.htmlsig.com/hc/en-us/sections/200647278-Installing-Signature", target="_blank"))]),
        ]),
        dbc.Col(width=2),
        dbc.Col(width=8)
    ])


    ]),
])