from flask import Flask

import requests
from flask import (
    Flask,
    Response,
    abort,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)

app = Flask(__name__)


@app.route('/')
def main_page():


    return 'hello'

@app.route('/v1/getsms')
def get_sms():
    pass

def send_sms(receptor, message):
    """ gets a MSISDN and a message, then uses KaveNegar to send sms."""
    url = f'https://api.kavenegar.com/v1/{config.API_KEY}/sms/send.json'
    data = {"message": message,
            "receptor": receptor}
    res = requests.post(url, data) # type: ignore

def check_serial():
    pass
