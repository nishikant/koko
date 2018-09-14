from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Boolean,
    Float,
)

from .meta import Base

class RentalPolicy(Base):
    __tablename__ = 'l_rental_policy'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer)
    active = Column(Integer, default=0) #1 is active
    version = Column(Integer)
    max_books = Column(Integer)
    loan_rate = Column(Float)

Index('category_idx', RentalPolicy.category_id, unique=True)

