# coding: utf-8
import os, sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask, render_template, request, url_for
from datetime import datetime

_wd = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)
