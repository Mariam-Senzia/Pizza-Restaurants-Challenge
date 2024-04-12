from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKeyConstraint, MetaData
# from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    # serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String ,unique=True, nullable=False)
    address = db.Column(db.String)

    pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade='all, delete-orphan')

    @db.validates('name')
    def valid_name(self,key , name):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters in length.")
        return name

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    # serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String)

    restaurants = db.relationship('RestaurantPizza', backref='pizza')

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurantpizzas'

    # serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer)
    price = db.Column(db.Float)

    __table_args__ = (
        ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ondelete='CASCADE'),
        ForeignKeyConstraint(['pizza_id'], ['pizzas.id'], ondelete='CASCADE'),
    )

    @db.validates('price')
    def validate_price(self, key, price):
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30.")
        return price