from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index():
  name = request.args.get("name", "World")
  return f'Hello, {escape(name)}!'
