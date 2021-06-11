from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# app initializqation
app = Flask(__name__)

# creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "very_secret"
db = SQLAlchemy(app)

from models.user import *

# initializing bcrypt
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if session['user']:
            user = User.query.filter_by(id=session['user']).first()
            return redirect('/home')
    except:
        if request.method == 'POST':
            email = request.form.get("email")
            password = request.form.get("password")
            user = User.query.filter_by(email=email).first()
            if user.email == email and bcrypt.check_password_hash(user.password, password):
                session['user'] = user.id
                return redirect('/home')
        return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        password = request.form.get("password")
        hashed_pw = bcrypt.generate_password_hash(password)

        user = User(fname=fname, lname=lname, email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()

    return render_template("register.html")

@app.route('/home')
def home(): 
    try:
        if session['user']:
            user = User.query.filter_by(id=session['user']).first()
            return render_template("home.html", name=user.fname)
    except:
        flash("You have to login first!")
        return redirect("/")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)