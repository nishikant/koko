from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Library(Base):
    __tablename__ = 'library'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    address = Column(Text)

Index('name_idx', Library.name, unique=True, mysql_length=255)
