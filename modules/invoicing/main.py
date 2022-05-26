import pdfkit
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import re



def generate_invoice():

    env = Environment(
        loader = FileSystemLoader("modules/invoicing/templates"),
        autoescape=select_autoescape()
    )

    time_now = re.sub('[^A-Za-z0-9]+', '', str(datetime.date.today()))
    

    rendered_string = env.get_template('template.html').render(
        sender_committee = 'IAESTE LC Lausanne',
        sender_name = 'Mirza Ćutuk',
        sender_address1 = 'Bd de Grancy 37',
        sender_address2 = '1006 Lausanne',
        sender_cc = '',
        invoice_nr = '1',
        sender_committee_short = 'LC Lausanne',
        invoice_date = str(datetime.date.today()),
        receive_committee = 'IAESTE LC Zurich',
        receive_address1 = 'Universitätstrasse 6',
        receive_address2 = '8092 Zürich',
        receive_cc = 'CAB E14',
        receive_committee_short = 'LC Zurich',
        invoice_subject = 'Accommodation Ski Weekend 2022',
        sender_pc = '10-181734-5',
        sender_address_full = 'IAESTE Local Committee Lausanne, Bd de Grancy 37, 1006 Lausanne',
        sender_iban = 'CH17 0900 0000 1018 1734 5',
        sender_bic = 'POFICHBEXXX',
        sender_phone = '+41 78 206 30 83',
        sender_email = 'cutukmirza@gmail.com'
        )
    
    filename = f'modules/invoicing/tmp/invoice{time_now}.html'
    f = open(filename, "w")
    f.write(rendered_string)
    f.close() 

    options = {
            'dpi': 400,
            'page-size': 'A4',
            'margin-top': '1in',
            'margin-right': '0in',
            'margin-bottom': '0in',
            'margin-left': '0in',
            'encoding': "UTF-8",
            'custom-header' : [
                ('Accept-Encoding', 'gzip')
            ],
            'no-outline': None,
            "enable-local-file-access": True
        }

    pdfkit.from_file(filename, "modules/invoicing/invoice_archive/temp1.pdf", verbose=True, options=options)
