from dash import html
import dash_bootstrap_components as dbc

from app.img import img
from app.models.db.member import Member
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

rows = [html.Tr([html.Td(member['name']), html.Td(member['city']), html.Td(member['company']), html.Td(member['email'])]) for member in Member.read_all()]
table_body = html.Tbody(rows)

alumni_layout = dbc.Row([
    dbc.Col(width=8,children=[
        html.Table(
            [
                html.Tr([html.Th('Name'), html.Th('City'), html.Th('Company'), html.Th('Email')]),
                table_body
                
            ],
            className='unselectable full-width alumni-table', id='member-table'
        )
    ]
    ),
    dbc.Col(width=4, children=[
        html.Img(src="data:image/png;base64,{}".format(img.profile_img.decode()),
        style={'width':'60%', 'margin':'auto', 'display':'block', 'borderRadius':'100%',}
        ),
        dbc.InputGroup(
            [dbc.InputGroupText("Name"), dbc.Input(),],
            className="mb-3 mt-3", id='sender-select'
        ),
        dbc.InputGroup(
            [dbc.InputGroupText("City"), dbc.Input()],
            className="mb-3", id='sender-select'
        ),
        dbc.InputGroup(
            [dbc.InputGroupText("Company"), dbc.Input(),],
            className="mb-3", id='sender-select'
        ),
        dbc.InputGroup(
            [dbc.InputGroupText("Email"), dbc.Input(),],
            className="mb-3", id='sender-select'
        ),
        dbc.InputGroup(
            [dbc.InputGroupText("Phone"), dbc.Input(),],
            className="mb-3", id='sender-select'
        ),
        dbc.InputGroup(
            [dbc.InputGroupText("Committee"), dbc.Input(),],
            className="mb-3", id='sender-select'
        ),
        dbc.InputGroup(
            [dbc.InputGroupText("Last Active"), dbc.Input(),],
            id='sender-select'
        ),
    ]

    )
])