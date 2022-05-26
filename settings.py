import datetime
import re

sender_committee = 'IAESTE LC Lausanne'
sender_name = 'Mirza Ćutuk'
sender_address1 = 'Bd de Grancy 37'
sender_address2 = '1006 Lausanne'
sender_cc = ''
invoice_nr = '1'
sender_committee_short = 'LC Lausanne'
invoice_date = re.sub('[^A-Za-z0-9]+', '', str(datetime.date.today()))
receive_committee = 'IAESTE LC Zurich'
receive_address1 = 'Universitätstrasse 6'
receive_address2 = '8092 Zürich'
receive_cc = 'CAB E14'
receive_committee_short = 'LC Zurich'
invoice_subject = 'Accommodation Ski Weekend 2022'
sender_pc = '10-181734-5'
sender_address_full = 'IAESTE Local Committee Lausanne, Bd de Grancy 37, 1006 Lausanne'
sender_iban = 'CH17 0900 0000 1018 1734 5'
sender_bic = 'POFICHBEXXX'
sender_phone = '+41 78 206 30 83'
sender_email = 'cutukmirza@gmail.com'