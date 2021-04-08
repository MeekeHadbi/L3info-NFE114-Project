from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask import g
from datetime import datetime, timedelta
import time


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'vaccinaction'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/connexion')
def login():
    return render_template("connexion.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
