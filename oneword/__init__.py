from flask import (
  Flask,
  jsonify,
  render_template
)
from flasgger import Swagger


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

  from oneword import site
  app.register_blueprint(site.app)

  from oneword import books
  app.register_blueprint(books.app)

  return app

if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)