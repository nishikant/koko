from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
)

from sqlalchemy.orm import relationship
from .meta import Base

class Category(Base):
    __tablename__ = 'l_category'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True) #convert to lower case before storing
    location = Column(Text) # Will help in physical search

    rental_policy_id = Column(
        Integer,
        ForeignKey('l_rental_policy.id', name='fk_category_rental_policy_id'),
        nullable=True,
    )

Index('cname_idx', Category.name, unique=True)

