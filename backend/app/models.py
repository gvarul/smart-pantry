from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=True)
    items = relationship("Item", back_populates="user")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Float, default=0.0)
    unit = Column(String, default="pcs")
    category = Column(String, nullable=True)
    purchase_date = Column(Date, nullable=True)
    expiry_date = Column(Date, nullable=True)
    barcode = Column(String, index=True, nullable=True)
    threshold = Column(Float, default=1.0)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="items")
    usage_logs = relationship("UsageLog", back_populates="item")
    shopping_list_entries = relationship("ShoppingList", back_populates="item")

class UsageLog(Base):
    __tablename__ = "usage_logs"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    used_quantity = Column(Float)
    used_date = Column(DateTime(timezone=True), server_default=func.now())
    remarks = Column(String, nullable=True)
    item = relationship("Item", back_populates="usage_logs")

class ShoppingList(Base):
    __tablename__ = "shopping_list"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    added_date = Column(DateTime(timezone=True), server_default=func.now())
    is_purchased = Column(Boolean, default=False)
    quantity = Column(Float, nullable=True)
    item = relationship("Item", back_populates="shopping_list_entries")
