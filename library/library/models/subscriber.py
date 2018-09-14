from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)

from .meta import Base

class Subscriber(Base):
    __tablename__ = 'l_subscriber'
    id = Column(Integer, primary_key=True)
    fname = Column(Text)
    lname = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    address = Column(Text)
    city = Column(Text)
    creation_date = Column(DateTime)
    status = Column(Integer)

Index('fname_idx', Subscriber.fname, mysql_length=255)
Index('lname_idx', Subscriber.lname, mysql_length=255)
Index('email_idx', Subscriber.email, mysql_length=255)

