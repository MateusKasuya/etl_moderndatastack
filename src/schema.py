from datetime import date
from typing import List

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt


class Customer_Schema(BaseModel):
    customer_id: PositiveInt
    name: str
    email: EmailStr
    phone: str
    address: str
    city: str
    state: str
    country: str
    join_date: date


class Customers_Schemas(BaseModel):
    customers: List[Customer_Schema]


class Product_Schema(BaseModel):
    product_id: PositiveInt
    product_name: str
    price: PositiveFloat
    stock_quantity: PositiveInt


class Products_Schemas(BaseModel):
    products: List[Product_Schema]


class Order_Schema(BaseModel):
    order_id: PositiveInt
    customer_id: PositiveInt
    product_id: PositiveInt
    order_date: date
    quantity: PositiveInt


class Orders_Schemas(BaseModel):
    orders: List[Order_Schema]
