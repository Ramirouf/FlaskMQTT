from flask import Flask, render_template, request, redirect, url_for, flash, session
import os, logging
from functools import wraps
from werkzeug.middleware.proxy_fix import ProxyFix
import paho.mqtt.publish as publish

logging.basicConfig(format='%(asctime)s - Ej2Flask - %(levelname)s - %(message)s', level=logging.INFO)

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route('/')
def index():
    return render_template('index.html')