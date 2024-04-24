# Flask Code Challenge - Pizza Restaurants
Welcome to the Flask Code Challenge for managing Pizza Restaurants! In this challenge, you'll be building out a Flask API to handle various functionalities related to Pizza Restaurants.

# Overview
Your task is to develop the Flask API to incorporate the functionalities outlined in the deliverables below. You'll need to implement routes, models, validations, and ensure proper handling of HTTP requests and responses.

# Models
You'll need to create the following relationships:

- A Restaurant has many Pizzas through RestaurantPizza.
- A Pizza has many Restaurants through RestaurantPizza.
- A RestaurantPizza belongs to a Restaurant and belongs to a Pizza.
- Start by creating the models and migrations for the specified database tables.

# Domain Model

## Validations
- Add validations to the RestaurantPizza model:

- Price must be between 1 and 30.
- Add validations to Restaurant model:

- Name must be less than 50 characters in length.
- Name must be unique.

# Routes
- Set up the following routes to handle different functionalities:

## GET /restaurants
- Returns JSON data containing a list of restaurants.

## GET /restaurants/:id
- Returns JSON data for a specific restaurant along with its pizzas if it exists.

## DELETE /restaurants/:id
- Deletes a restaurant from the database if it exists.

## GET /pizzas
- Returns JSON data containing a list of pizzas.

## POST /restaurant_pizzas
- Creates a new RestaurantPizza associated with an existing Pizza and Restaurant.

# Testing
Ensure to test your endpoints using Postman or any other REST API testing tool. Run the Flask server and make requests to validate the functionality of your API.

