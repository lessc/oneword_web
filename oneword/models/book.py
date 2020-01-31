from peewee import (
  CharField
)
from oneword.models import Base

class Book(Base):
  name = CharField()
