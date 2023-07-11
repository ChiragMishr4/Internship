from . import db 
from flask_login import UserMixin
from pymongo import MongoClient


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

client = MongoClient("mongodb://mongo:mongo@10.10.50.24:8001")
mydb = client['mydatabase']
mycol = mydb['customers']


