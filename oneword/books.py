from flask import (
  Blueprint,
  jsonify
)

app = Blueprint('books', __name__, url_prefix='/api/books')


@app.route('/')
def index():
  """获得书本列表
  ---
  responses:
    200:
      description: 'success'
  """
  books = [
    {'name': 'Python', 'price': 100},
    {'name': 'Python', 'price': 100},
    {'name': 'Python', 'price': 100}
  ]
  return jsonify(books)