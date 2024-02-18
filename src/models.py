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
    username = Column(String(120), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    favorites = relationship('Favorite', back_populates='user') # Relationship with favorites

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable = False)
    gender = Column(String(10))
    birth_year = Column(String(20))
    favorites = relationship('Favorite', back_populates='character')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    climate = Column(String(20))
    population = Column(Integer)

class UserFavorite(Base):
    __tablename__ = 'user_favorite'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    favorite_id = Column(Integer, ForeignKey('favorite.id'), primary_key=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship('User', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    
# UserFavorite table is the bridge that connects users to their favorite items
# while the Favorite table contains the details of each favorite item and its relationships.
# it's a way to handle many-to-many relationships in databases


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
