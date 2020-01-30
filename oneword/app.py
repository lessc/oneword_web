from flask import (
  Flask,
  jsonify,
  render_template
)
from flasgger import Swagger

APP_NAME = 'OneWord'

app = Flask(APP_NAME, template_folder="oneword/templates")
app.config['SWAGGER'] = {
  'title': f'{APP_NAME} APIs',
  'version': '0.1'
}
Swagger(app)


@app.route('/')
def index():
  site = {
    'name': 'OneWord'
  }
  return render_template('home/index.html', site=site)


@app.route('/api/books')
def books():
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


if __name__ == '__main__':
  app.run(debug=True)
