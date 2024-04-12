#!/usr/bin/env python3

from random import randint, choice as rc
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

pizza_types = [
    {"name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil"},
    {"name": "Pepperoni", "ingredients": "Pepperoni, Tomato sauce, Mozzarella"},
    {"name": "Hawaiian", "ingredients": "Ham, Pineapple, Tomato sauce, Mozzarella"},
    {"name": "Vegetarian", "ingredients": "Mushrooms, Bell peppers, Onions, Olives, Tomato sauce, Mozzarella"},
    {"name": "BBQ Chicken", "ingredients": "BBQ sauce, Chicken, Red onions, Cilantro, Mozzarella"},
    {"name": "Meat Lover", "ingredients": "Pepperoni, Sausage, Ham, Bacon, Tomato sauce, Mozzarella"},
    {"name": "Cheese", "ingredients": "Tomato sauce, Mozzarella"},
    {"name": "Supreme", "ingredients": "Pepperoni, Sausage, Mushrooms, Onions, Green peppers, Black olives, Tomato sauce, Mozzarella"},
    {"name": "Mushroom", "ingredients": "Mushrooms, Tomato sauce, Mozzarella"},
    {"name": "Ham & Cheese", "ingredients": "Ham, Cheese, Tomato sauce"},
    {"name": "Spicy", "ingredients": "Pepperoni, Jalapenos, Tomato sauce, Mozzarella"}
]

restaurant_data = [
    {"name": "Pizza Hut", "address": "123 Main St"},
    {"name": "Dominos", "address": "456 Elm St"},
    {"name": "Papa John's", "address": "789 Oak St"},
    {"name": "Little Caesars", "address": "101 Maple Ave"},
    {"name": "Pizza Place", "address": "202 Pine St"},
    {"name": "The Pizza Shop", "address": "303 Cedar St"},
    {"name": "Pizza Palace", "address": "404 Elm St"},
    {"name": "Pizza World", "address": "505 Oak St"},
    {"name": "Pizza Planet", "address": "606 Maple Ave"},
    {"name": "Pizza Galaxy", "address": "707 Pine St"},
    {"name": "Pizza Universe", "address": "808 Cedar St"}
]


with app.app_context():

    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    restaurants = [Restaurant(name=data['name'], address=data['address']) for data in restaurant_data]
    db.session.add_all(restaurants)
    db.session.commit()
    
    db.session.add_all(restaurants)
    db.session.commit()


    pizzas = [Pizza(name=pizza['name'], ingredients=pizza['ingredients']) for pizza in pizza_types]
    db.session.add_all(pizzas)
    db.session.commit()

    db.session.add_all(pizzas)
    db.session.commit()


    for restaurant in restaurants:
        for pizza in pizzas:
            price = randint(1, 30)
            rp = RestaurantPizza(restaurant_id=restaurant.id, pizza_id=pizza.id, price=price)
            db.session.add(rp)

    db.session.commit()
