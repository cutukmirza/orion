from dash import html, callback, Input, Output, State, no_update, dash_table
import dash_bootstrap_components as dbc
import datetime

from app.modules.invoicing.main import generate_invoice

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
    [
        dbc.InputGroup(
            [dbc.InputGroupText("Sender  "), dbc.Select(
                    options=[
                        {"label": "LC Lausanne", "value": 1},
                        {"label": "LC Zurich", "value": 2},
                    ]
                ),],
            className="mb-3", id='sender-select'
        ),
        dbc.InputGroup(
            [dbc.InputGroupText("Receiver"), dbc.Select(
                    options=[
                        {"label": "LC Lausanne", "value": 1},
                        {"label": "LC Zurich", "value": 2},
                    ]
                ),],
            className="mb-3", id='receiver-select'
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Invoice Subject"),
                dbc.Input(id='subject-input'),
                
            ],
            className="mb-3",
        ),
        dbc.Container(
            dbc.Row(
            [
                dash_table.DataTable(
                    id='invoice-table',
                    columns=[{
                        'name': '#',
                        'id': 'item-num',
                        #'deletable': True,
                        #'renamable': True
                    },
                    {
                        'name': 'Description',
                        'id': 'desc',
                    },
                    {
                        'name': 'Quantity',
                        'id': 'quant',
                    },
                    {
                        'name': 'Price',
                        'id': 'price',
                    },
                    {
                        'name': 'CHF',
                        'id': 'chf',
                    },  
                    ],
                    data=[
                        {'item-num': (1)}
                    ],
                    style_cell={'textAlign': 'right'},
                    editable=True,
                    row_deletable=True),
                html.Button(html.I(className="fas fa-plus-circle ml-2"), id='editing-rows-button', n_clicks=0, style={'fontSize':'20pt', 'color':'green', 'backgroundColor':'transparent', 'border':'None', 'position':'relative'}),
            ], justify='center'), 
            className="mb-3", style={"padding":"0"}),
        dbc.InputGroup(
            dbc.Button("Generate Invoice", color="success", id="generate-invoice-btn")
        )
    ]
),
            
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)

tabs_nav = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="New Invoice"),
        dbc.Tab(tab2_content, label="Invoice Archive"),
        dbc.Tab(
            "This tab's content is never seen", label="Tab 3", disabled=True
        ),
    ]
)

invoice_layout = html.Div(
    tabs_nav
)


sender_committee = 'IAESTE LC Lausanne'
sender_committee_short = 'LC Lausanne'
sender_name = 'Mirza Ćutuk'
sender_address1 = 'Bd de Grancy 37'
sender_address2 = '1006 Lausanne'
sender_cc = ''
sender_pc = '10-181734-5'
sender_address_full = 'IAESTE Local Committee Lausanne, Bd de Grancy 37, 1006 Lausanne'
sender_iban = 'CH17 0900 0000 1018 1734 5'
sender_bic = 'POFICHBEXXX'
sender_phone = '+41 78 206 30 83'
sender_email = 'cutukmirza@gmail.com'

invoice_nr = '1'
invoice_date = str(datetime.date.today())

receive_committee = 'IAESTE LC Zurich'
receive_committee_short = 'LC Zurich'
receive_address1 = 'Universitätstrasse 6'
receive_address2 = '8092 Zürich'
receive_cc = 'CAB E14'

invoice_subject = 'Accommodation Ski Weekend 2022'


@callback(
    Output(component_id='generate-invoice-btn', component_property='value'),
    Input(component_id='generate-invoice-btn', component_property='n_clicks'),

    Input(component_id='sender-select', component_property='value'),
    Input(component_id='receiver-select', component_property='value'),
    Input(component_id='subject-input', component_property='value'),

    Input(component_id='invoice-table', component_property='data'),

    prevent_initial_call = False
)
def gen_invoice(click, sender, receiver, subject, table_data):
    if click is not None:
        print(sender, receiver, subject, table_data)
        generate_invoice()
        return no_update

@callback(
    Output('invoice-table', 'data'),
    Input('editing-rows-button', 'n_clicks'),
    State('invoice-table', 'data'),
    State('invoice-table', 'columns'))
def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows