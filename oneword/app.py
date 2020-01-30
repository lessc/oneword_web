from flask import Flask, jsonify
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)


@app.route('/')
def index():
  return 'Hello, World!'


@app.route('/api/books')
def books():
  books = [
    {'name': 'Python', 'price': 100},
    {'name': 'Python', 'price': 100},
    {'name': 'Python', 'price': 100}
  ]
  return jsonify(books)


if __name__ == '__main__':
  app.run(debug=True)