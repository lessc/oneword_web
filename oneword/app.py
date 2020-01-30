from flask import (
  Flask,
  jsonify,
  render_template
)
from flasgger import Swagger


app = Flask(__name__, template_folder="")
Swagger(app)


@app.route('/')
def index():
  return 'Hello, World!'


@app.route('/api/books')
def books():
  """获得书本列表
  ---
  responses:
    200:
      description: A list of colors (may be filtered by palette)
  """
  books = [
    {'name': 'Python', 'price': 100},
    {'name': 'Python', 'price': 100},
    {'name': 'Python', 'price': 100}
  ]
  return jsonify(books)


if __name__ == '__main__':
  app.run(debug=True)
