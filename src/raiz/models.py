from datetime import date, datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Customer(Base):

    __tablename__ = 'customers'

    customer_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    address: Mapped[str]
    city: Mapped[str]
    state: Mapped[str]
    country: Mapped[str]
    join_date: Mapped[date]
    created_at: Mapped[datetime] = mapped_column(default=func.now())


class Product(Base):

    __tablename__ = 'products'

    product_id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str]
    price: Mapped[float]
    stock_quantity: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(default=func.now())


class Order(Base):

    __tablename__ = 'orders'

    order_id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(
        ForeignKey('customers.customer_id')
    )
    product_id: Mapped[int] = mapped_column(ForeignKey('products.product_id'))
    order_date: Mapped[date]
    quantity: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(default=func.now())
