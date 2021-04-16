#database models
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # the meal items are separate in order to add functionality to reorder or to do data analytics
    # the meal type ex: lunch, dinner, etc
    meal_type = db.Column(db.String(150))
    # main dish ordered
    main = db.Column(db.String(200))
    # side dish ordered
    side = db.Column(db.String(200))
    # drink ordered
    drink = db.Column(db.String(200))
    # dessert ordered if any
    dessert = db.Column(db.String(200))
    # order as string for easy printing
    order_string = db.Column(db.String(500))
    # date ordered
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # making each user have their own ordered page
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    
class User(db.Model, UserMixin):
    #self explanatory
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    orders = db.relationship('Order')
