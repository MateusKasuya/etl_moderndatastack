from datetime import date
from typing import List

from pydantic import BaseModel, EmailStr, PositiveInt


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
