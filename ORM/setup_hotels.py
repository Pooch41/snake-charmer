from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///data/hotels.sqlite')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Hotel(Base):
    __tablename__ = 'hotels'

    hotel_id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_name = Column(String)
    hotel_city = Column(String)

    def __repr__(self):
        return (f"Hotel(hotel_id = {self.hotel_id}, name = {self.hotel_name}, "
                f"city = {self.hotel_city})")


Base.metadata.create_all(engine)

hotel = Hotel(
    hotel_name="Capella Bangkok",
    hotel_city="Bangkok, TH",
)

session.add(hotel)

hotel = Hotel(
    hotel_name="Passalacqua",
    hotel_city="Lake Como, IT",
)

session.add(hotel)

hotel = Hotel(
    hotel_name="Rosewood Hong Kong",
    hotel_city="Hong Kong, CH",
)

session.add(hotel)

session.commit()
