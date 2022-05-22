from flask import Flask
from threading import Thread


app = Flask('')


@app.route('/')
def index():
    return 'Online'


def run():
    app.run(host='0.0.0.0', port=8081)


def active():
    Thread(target=run).start()