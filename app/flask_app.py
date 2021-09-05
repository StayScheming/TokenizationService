from flask import json, Flask, request

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)