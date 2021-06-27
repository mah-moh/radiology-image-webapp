from flask import Flask, render_template, url_for, request, redirect, session, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
import os

# app initializqation
app = Flask(__name__)

# initializing bcrypt
bcrypt = Bcrypt(app)

# assigning upload path and allowed extensions
UPLOAD_FOLDER = 'app/static/upload_files'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "very_secret"\
# creating database
db = SQLAlchemy(app)

from app import views