from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    
    # Define the one-to-many relationship with Review
    reviews = relationship('Review', back_populates='restaurant')
    
    # Define the many-to-many relationship with Customer
    customers = relationship('Customer', secondary='reviews', overlaps='restaurants')

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
    # Define the one-to-many relationship with Review
    reviews = relationship('Review', back_populates='customer')
    
    # Define the many-to-many relationship with Restaurant
    restaurants = relationship('Restaurant', secondary='reviews', overlaps='customers')

class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    star_rating = Column(Integer)
    
    # Define the many-to-one relationship with Customer
    customer = relationship('Customer', back_populates='reviews')
    
    # Define the many-to-one relationship with Restaurant
    restaurant = relationship('Restaurant', back_populates='reviews', overlaps='customers')
    
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars"
