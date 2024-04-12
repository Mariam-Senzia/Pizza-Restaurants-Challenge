#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

from models import db , Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Restaurant/Pizza/RestaurantPizza API"

@app.route('/restaurants')
def get_restaurants():

    restaurants = []
    for rest in Restaurant.query.all():
        rest_dict = {
            "id" : rest.id,
            "name": rest.name,
            "address": rest.address
        }
        restaurants.append(rest_dict)

    response = make_response(
        restaurants,
        200
    )

    return response

#restaurant by id
@app.route('/restaurants/<int:id>')
def get_restaurants_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()

    if restaurant:
        rest_dict = {
                "id" : restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        
        response = make_response(
            rest_dict,
            200
        )
        return response

    else:
        return jsonify({"error": "Restaurant not found"}), 404

#delete
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurants(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()

    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Review deleted."
        }

        response = make_response(
                response_body,
                200
            )

        return response
    
    else:
        return jsonify({"error": "Restaurant not found"}), 404
    
#pizzas
@app.route('/pizzas')
def get_pizzas():

    pizzas = []
    for pizza in Pizza.query.all():
        pizza_dict = {
            "id" : pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        pizzas.append(pizza_dict)

    response = make_response(
        pizzas,
        200
    )

    return response

#restaurant_pizzas
@app.route('/restaurant_pizzas', methods=['POST'])
def add_restaurant_pizzas():

    new_restaurant_pizza = RestaurantPizza(
            price=float(request.form.get("price")),
            pizza_id=request.form.get("pizza_id"),
            restaurant_id=request.form.get("restaurant_id"),
        )
    if new_restaurant_pizza:
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        restaurant_pizza_dict = restaurant_pizza_dict = {
        'id': new_restaurant_pizza.id,
        'price': new_restaurant_pizza.price,
        'pizza_id': new_restaurant_pizza.pizza_id,
        'restaurant_id': new_restaurant_pizza.restaurant_id
    }
# jsonify(new_restaurant_pizza)

        response = make_response(
            jsonify(restaurant_pizza_dict),
            201
        )

        return response
    
    else:
        return jsonify({"errors" : ["validation errors"]}),400




if __name__ == '__main__':
    app.run(port=5555, debug=True)