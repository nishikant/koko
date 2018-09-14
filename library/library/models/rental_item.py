from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    Boolean,
)

from .meta import Base

class RentalItem(Base):
    __tablename__ = 'l_rental_item'
    id = Column(Integer, primary_key=True)
    subscriber_id = Column(Integer)
    category_id = Column(Integer)
    rental_policy_version = Column(Integer) #Set to current active policy for category
    book_id = Column(Integer)
    borrowed_date = Column(DateTime)
    loan_period = Column(Integer)
    overdue = Column(Integer, default=0)
    status = Column(Integer)

Index('rsubscriber_idx', RentalItem.subscriber_id)
Index('rcategory_idx', RentalItem.category_id)
Index('rbook_idx', RentalItem.book_id)

