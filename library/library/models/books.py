from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Float,
    Boolean,
    ForeignKey,
)

from .meta import Base

class Books(Base):
    __tablename__ = 'l_books'
    id = Column(Integer, primary_key=True)
    category_id = Column(
        Integer,
        ForeignKey('l_category.id', name='fk_category'),
        nullable=True,
    )
    isbn = Column(Text)
    name = Column(Text)
    overview = Column(Text)
    edition = Column(Integer)
    author = Column(Text)
    format = Column(Text)
    count = Column(Integer)
    max_price = Column(Float) #max price of one book. to be used in case it is lost
    instock = Column(Boolean(name='instock_flag'))

Index('bname_idx', Books.name, unique=True, mysql_length=255)
Index('isbn_idx', Books.isbn, unique=True, mysql_length=255)
Index('author_idx', Books.isbn, unique=True, mysql_length=255)

