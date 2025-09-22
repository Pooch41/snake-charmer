from sqlalchemy import create_engine, Column, Integer, String, update
from setup import session, Restaurant

restaurant_to_update = session.query(Restaurant) \
    .filter(Restaurant.restaurant_name == "NYC Diner") \
    .one()
restaurant_to_update.famous_dish = "French Toast and Bacon"
session.commit()