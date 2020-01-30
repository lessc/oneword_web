from flask import (
  Blueprint,
  render_template
)

app = Blueprint('site', __name__)

@app.route('/')
def index():
  site = {
    'name': 'OneWord'
  }
  return render_template('site/index.html', site=site)
