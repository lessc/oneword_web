from peewee import (
  MySQLDatabase,
  Model,
  CharField
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