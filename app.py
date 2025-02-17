import datetime
from flask import Flask


app = Flask(__name__)


@app.route('/')
def view():
    current_time = datetime.datetime.now()
    return current_time


if __name__ == '__main__':
    app.run(port=5080, debug=True, host='0.0.0.0')
