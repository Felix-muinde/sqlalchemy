
from faker import Faker
from main import Customer
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

Base =  declarative_base()
engine = create_engine('sqlite:///Felix_database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

fake=Faker()
customers = [
    Customer(
        first_name= fake.name(),
        last_name= fake.name()
        
    )
    for i in range(20)]

session.bulk_save_objects(customers)
session.commit()

fake=Faker()
restaurants = [
    restaurants(
        name= fake.name(),
        price= fake.price()
        
    )
    for i in range(20)]

session.bulk_save_objects(restaurants)
session.commit()

fake=Faker()
reviews = [
    reviews(
        customer_name= fake.name(),
        restaurant_name= fake.name()
        
    )
    for i in range(20)]

session.bulk_save_objects(reviews)
session.commit()