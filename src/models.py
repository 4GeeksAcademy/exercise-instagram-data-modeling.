import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship, declarative_base, DeclarativeBase
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(12), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)


followers = Table(
    "followers",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_from_id", ForeignKey("user.id")),
    Column("user_to_id", ForeignKey("user.id")),
)


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"))


class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    post_id = Column(ForeignKey("post.id"), nullable=False)
    url = Column(String, nullable=False)
    type = Column(String, nullable=False)


comments = Table(
    "comments",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("comment", String, nullable=False),
    Column("post_id", ForeignKey("post.id"), nullable=False),
    Column("author_id", ForeignKey("user.id"), nullable=False),
)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, "diagram.png")
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise 