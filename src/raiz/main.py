from database import Base, engine
from models import Customer, Product, Order


Base.metadata.create_all(engine)