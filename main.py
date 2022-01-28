from flask import Flask, request, make_response, escape, redirect

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    user_ip = escape(user_ip)
    return f"Hello World Flask, IP {user_ip}"
