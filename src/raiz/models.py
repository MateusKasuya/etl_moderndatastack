from datetime import datetime

from database import Base
from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)

class Customer(Base):

    __tablename__ = 'customers'

    def __init__(
        self,
        name,
        email,
        phone,
        address,
        city,
        state,
        country,
        join_date,
        created_at=datetime.now(),
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.join_date = join_date
        self.created_at = created_at

    customer_id = Column('customer_id', Integer, primary_key=True)   # 1
    name = Column('name', String)   # "Julian Johnston"
    email = Column('email', String)   # "rbaker@example.org"
    phone = Column('phone', String)   # "(253)781-2504"
    address = Column(
        'addres', String
    )   # "537 Townsend Valley Apt. 824\nNew Leslie, NM 82307"
    city = Column('city', String)   # "Lake Brittney"
    state = Column('state', String)   # "North Dakota"
    country = Column('country', String)   # "Niue"
    join_date = Column('join_date', Date)   # "2021-05-23"
    created_at = Column('created_at', DateTime)   # datetime.now()


class Product(Base):

    __tablename__ = 'products'

    def __init__(
        self, product_name, price, stock_quantity, created_at=datetime.now()
    ):
        self.product_name = product_name
        self.price = price
        self.stock_quantity = stock_quantity
        self.created_at = created_at

    product_id = Column('product_id', Integer, primary_key=True)   # 1
    product_name = Column('product_name', String)   # "Inside"
    price = Column('price', Float)   # 559.99
    stock_quantity = Column('stock_quantity', Integer)   # 214
    created_at = Column('created_at', DateTime)   # datetime.now()


class Order(Base):

    __tablename__ = 'orders'

    def __init__(
        self,
        customer_id,
        product_id,
        order_date,
        quantity,
        created_at=datetime.now(),
    ):
        self.customer_id = customer_id
        self.product_id = product_id
        self.order_date = order_date
        self.quantity = quantity
        self.created_at = created_at

    order_id = Column('order_id', Integer, primary_key=True)   # 1
    customer_id = Column(
        'customer_id', Integer, ForeignKey('customers.customer_id')
    )   # 41
    product_id = Column(
        'product_id', Integer, ForeignKey('products.product_id')
    )   # 879
    order_date = Column('order_date', Date)   # "2024-06-06"
    quantity = Column('quantity', Integer)   # 7
    created_at = Column('created_at', DateTime)   # datetime.now()
