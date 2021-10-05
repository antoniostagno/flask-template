from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


class Error(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# URLs
@app.route('/')
def index():
    age = 57
    return f"Ceci est le premier serveur de Antonio, qui a {age} ans"


@app.errorhandler(Error)
def error(error):
    return jsonify({
        "success": False,
        'error': error.status_code,
        "message": error.error,
    }), error.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # serve(app, port=80)
