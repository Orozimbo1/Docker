import flask
from flask import Flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=["GET"])
def indexx():
    return '<h1>Hello Kubernets!!!</h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")
