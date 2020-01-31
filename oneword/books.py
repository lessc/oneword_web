from flask import (
  request,
  Blueprint,
  jsonify
)
from oneword.models.book import Book
from playhouse.shortcuts import model_to_dict


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

  books = list(map(model_to_dict, data))
  return jsonify(books)

@app.route('/', methods=['POST'])
def save():
  """创建一本书
  ---
  parameters: 
    - in: body
      name: body
      schema:
        id: Book
        required:
          - name
          - price
        properties:
          name:
            type: string
            description: 书名
          price:
            type: number
            description: 价格
  responses: 
    200:
      description: 'success'
  """

  param = request.json
  book = Book(name=param['name'], price=param['price'])
  success = book.save()
  if (success):
    return jsonify({'success': True, 'data': model_to_dict(book)})
  else:
    return jsonify({'success': False, 'message': '保存失败'})

@app.route('/<id>', methods=['DELETE'])
def delete(id):
  """删除一本书
  ---
  parameters:
    - in: path
      name: id
      type: string
      required: true
  responses:
    200:
      description: 'success'
  """
  success = Book.delete_by_id(id) > 0
  return jsonify({'success': success})