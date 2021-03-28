from flask import Flask, render_template
from flask import g
from datetime import datetime, timedelta
import time


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
