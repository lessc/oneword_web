from flask import (
  g,
  Flask,
  jsonify,
  render_template
)
from flasgger import Swagger
from oneword.models import db


def create_app():
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='EBCB35E1-BCF3-46BE-BF7E-88E428549779'
  )
  app.config['SWAGGER'] = {
    'title': 'OneWord APIs',
    'version': '0.1'
  }
  Swagger(app)

  app.before_request(lambda: before_request(app))
  app.teardown_request(lambda ex: teardown_request(app, ex))

  from oneword import site
  app.register_blueprint(site.app)

  from oneword import books
  app.register_blueprint(books.app)

  return app


def before_request(app):
  db.connect()

def teardown_request(app, ex):
  db.close()