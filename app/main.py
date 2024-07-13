from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():


    return 'hello'

@app.route('/v1/getsms')
def get_sms():
    pass

def send_sms():
    pass

def check_serial():
    pass
