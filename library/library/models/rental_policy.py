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
    name = Column(Text, unique=True)
    category_id = Column(Integer)
    active = Column(Boolean(name='active_bool'), default=False)
    version = Column(Integer)
    max_books = Column(Integer)
    loan_rate = Column(Float)
    min_rate = Column(Float, default=0)
    min_days = Column(Float, default=0)

Index('category_idx', RentalPolicy.category_id, unique=True)
Index('rpname_idx', RentalPolicy.name, unique=True)

