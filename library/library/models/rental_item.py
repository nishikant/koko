from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    Boolean,
    ForeignKey,
)

from .meta import Base

class RentalItem(Base):
    __tablename__ = 'l_rental_item'
    id = Column(Integer, primary_key=True)

    subscriber_id = Column(
        Integer,
        ForeignKey('l_subscriber.id', name='fk_subscriber')
    )

    category_id = Column(
        Integer,
        ForeignKey('l_category.id', name='fk_rentalitem'),
    )

    book_id = Column(
        Integer,
        ForeignKey('l_books.id', name='fk_book')
    )

    rental_policy_version = Column(Integer) #Set to current active policy for category
    borrowed_date = Column(DateTime)
    loan_period = Column(Integer)
    status = Column(Integer)

Index('rsubscriber_idx', RentalItem.subscriber_id)
Index('rcategory_idx', RentalItem.category_id)
Index('rbook_idx', RentalItem.book_id)

