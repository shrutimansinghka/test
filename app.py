import csv
import zipfile

import requests
from flask import Flask, session, render_template, request, url_for, g, send_from_directory
import config
from werkzeug.utils import redirect

from database import Database



app = Flask(__name__)
app.secret_key = config.secret_key


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/download', methods= ['GET'])
def download():
    zip_ref = zipfile.ZipFile('/Users/shrutimansinghka/Downloads/NB69590001_00000_18022018_160501_Trigger.zip', 'r')
    zip_ref.extractall('/Users/shrutimansinghka', pwd=bytes(config.pwd, 'utf-8'));
    zip_ref.close()

    # style = xlwt.XFStyle()
    # style.num_format_str = '#,###0.00'

    txt_file = r"/Users/shrutimansinghka/NB69590001_00000_18022018_160501_Trigger.txt"
    csv_file = r"/Users/shrutimansinghka/NB69590001_00000_18022018_160501_Trigger.csv"

    # f = open('/Users/shrutimansinghka/NB69590001_00000_18022018_160501_Trigger.txt', 'r+')
    in_txt = csv.reader(open(txt_file, "rt"), delimiter=config.delimiter)
    out_csv = csv.writer(open(csv_file, 'wt'))

    out_csv.writerows(in_txt)
    return send_from_directory('/Users/shrutimansinghka', filename='NB69590001_00000_18022018_160501_Trigger.csv')


app.run(port=4995,debug=True)