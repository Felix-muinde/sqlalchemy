from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base, Customer, Restaurant, Review

# Define the database URL
db_url = 'sqlite:///Felix_database.db'

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Create tables in the database based on the defined models
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create instances and add them to the session
customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Alice", last_name="Johnson")

restaurant1 = Restaurant(name="Restaurant A", price=4)
restaurant2 = Restaurant(name="Restaurant B", price=3)

review1 = Review(customer=customer1, restaurant=restaurant1, star_rating=5)
review2 = Review(customer=customer2, restaurant=restaurant1, star_rating=4)
review3 = Review(customer=customer1, restaurant=restaurant2, star_rating=3)
review4 = Review(customer=customer2, restaurant=restaurant2, star_rating=2)

session.add_all([customer1, customer2, restaurant1, restaurant2, review1, review2, review3, review4])
session.commit()

# Close the session
session.close()
