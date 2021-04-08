from flask import Flask, render_template, request
from flask import g
from datetime import datetime, timedelta
import time
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'vaccinaction'

mysql = MySQL()
mysql.init_app(app)

def get_all_appointments():
    
    cursor = mysql.get_db().cursor()
    datas = cursor.execute("select * from data_poseidon ORDER BY id DESC")
    str(datas)
    return datas

def connect_db():
    
    return connection

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
