from flask import Flask, render_template, redirect, request, session
import sqlite3
from sqlite3 import Error
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "kzgsdlit3e"

@app.route('/')
def render_home():
    return render_template('home.html')


app.run(host='0.0.0.0', debug=True)
