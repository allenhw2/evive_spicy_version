#Evive Take Home Allen Wang 2021
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Order
from . import db
import json

views = Blueprint('views', __name__)

class Meal:
    #order class indentifies the type of order and creates the object
    #order class also prints the order 
    def __init__(self, mealType, main, side, drink, dessert):
        self.error = 0
        self.mealType = mealType
        if drink == '':
            drink = "water"
        if mealType == "breakfast":
            self.meal = Breakfast(main, side, drink, dessert)
        elif mealType == "lunch":
            self.meal = Lunch(main, side, drink, dessert)
        elif mealType == "dinner":
            self.meal = Dinner(main, side, drink, dessert)
        else:
            #if the meal type is invalid, it will raise Exception
            flash('Unknown Meal Type', category='error')
            self.error = 1
            #error handling

    def print(self):
        if self.meal == None:
            flash('Unknown Meal Type', category='error')
            return ""
        return self.meal.print();


class Lunch():
    def __init__(self, main, side, drink, dessert):

        #keeping a dict of the menu so that it can be added to for scalability
        self.lunch_menu = {
            "main": ["salad"],
            "side": ["chips"],
            "drink": ["soda", "water"]
        }

        #list of main dishes ordered in format of item name
        self.main = main
        #list of side dishes ordered in format of item name
        self.side = side
        #list of drinks ordered in format of item name
        self.drink = drink
        self.dessert = dessert
        self.error = 0

        if main not in self.lunch_menu["main"]:
            flash('Unknown main dish', category='error')
            self.error = 1;
        if side not in self.lunch_menu["side"]:
            flash('Unknown side dish', category='error')
            self.error = 1;
        if drink not in self.lunch_menu["drink"]:
            flash('Unknown drink, replaced with water', category='success')
            self.drink = "water"

    
    def print(self):

        #if there were any errors in the order found, print them
        if self.error:
            return ''
        
        #printing the correct format of order\
        return (f"Mealtype: Lunch   Main Dish: {self.main}  Side Dish: {self.side}  Drink: {self.drink}")



class Dinner():
    def __init__(self, main, side, drink, dessert):

        #keeping a dict of the menu so that it can be added to for scalability
        self.dinner_menu = {
            "main": ["steak"],
            "side": ["potatoes"],
            "drink": ["wine", "water"],
            "dessert": ["cake"] 
        }

        #list of main dishes ordered in format of item name
        self.main = main
        #list of side dishes ordered in format of item name
        self.side = side
        #list of drinks ordered in format of item name
        self.drink = drink

        self.dessert = dessert
        self.error = 0

        if main not in self.dinner_menu["main"]:
            flash('Unknown main dish', category='error')
            self.error = 1;
        if side not in self.dinner_menu["side"]:
            flash('Unknown side dish', category='error')
            self.error = 1;
        if drink not in self.dinner_menu["drink"]:
            flash('Unknown drink, replaced with water', category='success')
            self.drink = "water"
        if dessert not in self.dinner_menu["dessert"]:
            flash('Unknown dessert', category='error')
            self.error = 1;

    
    def print(self):
        #if there were any errors in the order found, print them
        if self.error:
            return ''
        #printing the correct format of order\
        return (f"Mealtype: Dinner   Main Dish: {self.main}  Side Dish: {self.side}  Drink: {self.drink}    Dessert:{self.dessert}")

class Breakfast():
    def __init__(self, main, side, drink, dessert):
        #keeping a dict of the menu so that it can be added to for scalability
        self.lunch_menu =  {
            "main": ["eggs"],
            "side": ["toast"],
            "drink": ["coffee", "water"]
        }

        #list of main dishes ordered in format of item name
        self.main = main
        #list of side dishes ordered in format of item name
        self.side = side
        #list of drinks ordered in format of item name
        self.drink = drink
        self.dessert = dessert
        self.error = 0

        if main not in self.lunch_menu["main"]:
            flash('Unknown main dish', category='error')
            self.error = 1;
        if side not in self.lunch_menu["side"]:
            flash('Unknown side dish', category='error')
            self.error = 1;
        if drink not in self.lunch_menu["drink"]:
            flash('Unknown drink, replaced with water', category='success')
            self.drink = "water"

    
    def print(self):
        #if there were any errors in the order found, print them
        if self.error:
            return ''
        #printing the correct format of order\
        return (f"Mealtype: Lunch   Main Dish: {self.main}  Side Dish: {self.side}  Drink: {self.drink}")

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        mealType = request.form.get('mealType').strip().lower()
        main = request.form.get('main').strip().lower()
        side = request.form.get('side').strip().lower()
        drink = request.form.get('drink').strip().lower()
        dessert = request.form.get('dessert').strip().lower()

        if mealType != 'dinner' and dessert != '':
            flash('You are not allowed to order dessert at this time', category = 'error')
        else:
            new_meal = Meal(mealType, main, side, drink, dessert)
            if new_meal.error:
                flash('Error found in order', category = 'error')
                return render_template("home.html", user=current_user)
            meal_string = new_meal.print()
            if meal_string == '':
                flash('Error found in order', category = 'error')
                return render_template("home.html", user=current_user)
            new_order = Order(
                meal_type=new_meal.mealType,
                main=new_meal.meal.main,
                side=new_meal.meal.side,
                drink=new_meal.meal.drink,
                dessert=new_meal.meal.dessert,
                order_string=meal_string,
                user_id = current_user.id
                )
            db.session.add(new_order)
            db.session.commit()
            flash('Meal ordered', category = 'success')

    return render_template("home.html", user=current_user)

@views.route('/delete-order', methods=['POST'])
def delete_order():
    order = json.loads(request.data)
    orderId = order['orderId']
    order = Order.query.get(orderId)
    if order:
        if order.user_id == current_user.id:
            db.session.delete(order)
            db.session.commit()
            
    return jsonify({})

