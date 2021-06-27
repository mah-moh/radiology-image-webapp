from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    file_path = db.relationship('Filepath', backref='owener')

class Filepath(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(80), nullable=False)
    user_id = db.Column((db.Integer), db.ForeignKey("user.id")) # adding User.id as a foreign key