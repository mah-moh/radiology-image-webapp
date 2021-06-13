from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# app initializqation
app = Flask(__name__)

# initializing bcrypt
bcrypt = Bcrypt(app)

# creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "very_secret"
db = SQLAlchemy(app)

from app import views