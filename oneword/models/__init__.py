from datetime import datetime
from peewee import (
  MySQLDatabase,
  Model,
  AutoField,
  DateTimeField
)

HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
PASS = 'root'
DB = 'oneword_dev'

db = MySQLDatabase(DB, host=HOST, port=PORT, user=USER, password=PASS)

class Base(Model):
  class Meta:
    database = db

  id = AutoField()
  created = DateTimeField(default=datetime.now())
  updated = DateTimeField()

  def save(self, *args, **kwargs):
    self.updated = datetime.now()
    return super(Base, self).save(*args, **kwargs)