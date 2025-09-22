from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///data/restaurants.sqlite')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurants'

    restaurant_id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_name = Column(String)
    restaurant_city = Column(String)
    famous_dish = Column(String)

    def __repr__(self):
        return f"Restaurant(restaurant_id = {self.restaurant_id}, name = {self.restaurant_name})"


Base.metadata.create_all(engine)

# restaurant = Restaurant(
#     restaurant_name="NYC Diner",
#     restaurant_city="New York City, US",
#     famous_dish="Eggs Benedict"
# )
# session.add(restaurant)
#
# restaurant = Restaurant(
#     restaurant_name="The French Laundry",
#     restaurant_city="Yountville, US",
#     famous_dish="Oysters and Pearls"
# )
#
# session.add(restaurant)
#
# restaurant = Restaurant(
#     restaurant_name="THE FAT DUCK",
#     restaurant_city="BRAY, UK",
#     famous_dish="Snail Porridge"
# )
#
# session.add(restaurant)
#
# restaurant = Restaurant(
#     restaurant_name="EL CELLER DE CAN ROCA",
#     restaurant_city="GIRONA, ESP",
#     famous_dish="Green olive's ice cream and black olive tempura"
# )
#
# session.add(restaurant)
#
# session.commit()
