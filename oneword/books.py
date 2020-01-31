from flask import (
  Blueprint,
  jsonify
)
from oneword.models import db
from oneword.models.book import Book

app = Blueprint('books', __name__, url_prefix='/api/books')


@app.route('/', methods=['GET'])
def index():
  """获得书本列表
  ---
  responses:
    200:
      description: 'success'
  """
  db.connect()
  books = [
    {'name': 'Python', 'price': 100},
    {'name': 'Python', 'price': 100},
    {'name': 'Python', 'price': 100}
  ]
  return jsonify(books)

@app.route('/', methods=['POST'])
def save():
  """创建一本书
  ---
  responses: 
    200:
      description: 'success'
  """
  return success()

@app.route('/<id>', methods=['DELETE'])
def delete(id):
  """删除一本书
  ---
  parameters:
    - name: id
      in: path
      type: string
      required: true
  responses:
    200:
      description: 'success'
  """
  return success()

def success(data = None):
  return jsonify({'success': True, 'data': data})
