from io import BytesIO
import json
from flask import Flask, render_template, request, session, send_file
import jinja2
env = jinja2.Environment()
env.globals.update(zip=zip)
import requests
from flask import request
import ast
app = Flask(__name__)


@app.route('/analyze', methods=['GET'])
def analyze():
    # get track id