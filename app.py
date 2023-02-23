from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='static')

@app.errorhandler(404)
def not_found(e):
    return "ILTPWC 404"

@app.route("/")
def index():
    return app.send_static_file("index.html")
