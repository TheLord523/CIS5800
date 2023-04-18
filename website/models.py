#from this package, import db
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #references User.id primary key

class User(db.Model, UserMixin): #UserMixin to access the current_user object/all the information about the currently logged in user in the auth.py
    #you're almost always going to have db.Column
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True) #no user can have the same email as another
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship('Note')