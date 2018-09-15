from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
)
from sqlalchemy.dialects.sqlite import DATETIME

from .meta import Base
import datetime

class Subscriber(Base):
    __tablename__ = 'l_subscriber'
    id = Column(Integer, primary_key=True)
    fname = Column(Text)
    lname = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    address = Column(Text)
    city = Column(Text)
    creation_date = Column(DATETIME, default=datetime.datetime.now)
    status = Column(Integer)
    library_id = Column(
        Integer,
        ForeignKey('library.id', name='fk_library'),
        nullable=True,
    )

Index('fname_idx', Subscriber.fname, mysql_length=255)
Index('lname_idx', Subscriber.lname, mysql_length=255)
Index('email_idx', Subscriber.email, mysql_length=255)

