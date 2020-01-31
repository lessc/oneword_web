from flask import (
  request,
  Blueprint,
  jsonify
)
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
  page = int(request.args.get('page', '1'))
  limit = 20

  data = (Book.select()
    .order_by(Book.id.desc())
    .paginate(page, limit)
  ).execute()
  
  books = [{
    'id': book.id,
    'name': book.name,
    'price': book.price
  } for book in data]

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
