from flask import Flask, jsonify

app = Flask(__name__)

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