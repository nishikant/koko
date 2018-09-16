from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
)

from .meta import Base

class LibraryCategory(Base):
    __tablename__ = 'l_library_category'
    id = Column(Integer, primary_key=True)

    library_id = Column(
        Integer,
        ForeignKey('library.id', name='fk_category_rental_policy_id'),
        nullable=True,
    )

    category_id = Column(
        Integer,
        ForeignKey('l_category.id', name='fk_category_rental_policy_id'),
        nullable=True,
    )

Index('l_idx', LibraryCategory.library_id, mysql_length=255)
Index('c_idx', LibraryCategory.category_id, mysql_length=255)
