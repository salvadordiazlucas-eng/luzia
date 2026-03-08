from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    locations = relationship("Location", back_populates="restaurant")


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    name = Column(String, nullable=False)
    address = Column(String)
    city = Column(String)
    capacity = Column(Integer)

    restaurant = relationship("Restaurant", back_populates="locations")
    tables = relationship("Table", back_populates="location")


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    name = Column(String)
    seats = Column(Integer)

    location = relationship("Location", back_populates="tables")


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))

    customer_name = Column(String)
    customer_phone = Column(String)
    guests = Column(Integer)

    reservation_time = Column(DateTime)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
