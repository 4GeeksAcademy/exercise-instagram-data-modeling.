import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(90), unique=True, nullable=False)
    relacion_posts= relationship("post", backref="user", lazy=True)
    relacion_commnet= relationship("commnet", backref="user", lazy=True)
    relacion_followers= relationship("followers", backref="user", lazy=True)
    relacion_media= relationship("media", backref="user", lazy=True)
    



class Post(Base):
     __tablename__ = 'post'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))
     relacion_comment= relationship("comment", backref="user", lazy=True)

class Comment (Base):
        __tablename__ = 'comment'
        id=Column (Integer, primary_key=True)
        coment_text=Column(String(250))
        author_id=Column(Integer, ForeignKey("user.id"))
        post_id = Column(Integer, ForeignKey("post.id"))

class Followers(Base):
         __tablename__ = 'followers'
         id=Column(Integer, primary_key=True)
         user_from_id=Column(Integer, ForeignKey("user.id"))
         user_to_id=Column(Integer, ForeignKey("user.id"))

class Media (Base):
        __tablename__ = 'follower'
        id=Column(Integer, primary_key=True)
        post_id=Column(Integer, ForeignKey("user.id"))

    


   
   

    

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
