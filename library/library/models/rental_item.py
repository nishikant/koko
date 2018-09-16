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

    rental_policy_id = Column(
        Integer,
        ForeignKey('l_rental_policy.id', name='fk_rental_policy_item')
    )

    #Set to current active policy for category
    borrowed_date = Column(DateTime)
    loan_period = Column(Integer)
    return_date = Column(DateTime, default=None)
    status = Column(Integer) #1, rented,

Index('rsubscriber_idx', RentalItem.subscriber_id)
Index('rcategory_idx', RentalItem.category_id)
Index('rbook_idx', RentalItem.book_id)

