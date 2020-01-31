from peewee import (
  AutoField,
  CharField,
  DoubleField,
  DateTimeField
)
from oneword.models import Base

class Book(Base):
  name = CharField()
  price = DoubleField()
