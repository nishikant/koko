from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Float,
    Boolean,
)

from .meta import Base

class Books(Base):
    __tablename__ = 'l_books'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer)
    isbn = Column(Text)
    name = Column(Text)
    overview = Column(Text)
    edition = Column(Integer)
    author = Column(Text)
    format = Column(Text)
    count = Column(Integer)
    max_price = Column(Float) #max price of one book. to be used in case it is lost
    instock = Column(Integer, default=1)

Index('bname_idx', Books.name, unique=True, mysql_length=255)
Index('isbn_idx', Books.isbn, unique=True, mysql_length=255)
Index('author_idx', Books.isbn, unique=True, mysql_length=255)

