import flask
from flask import request, json, jsonify
import requests
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def index():
    data = requests.get("https://randomuser.me/api")
    return data.json()

@app.route("/inserthost/", methods=["POST"])
def inserthost():
    data = requests.get("https://randomuser.me/api").json()
    username = data["results"][0]["name"]["first"]

    connection = psycopg2.connect(
        host ="postgres_api_container",
        port= 5432,
        user="postgres",
        password="postgres",
        database="flaskdocker"
    )


    cursor = connection.cursor()

    cursor.execute("""INSERT INTO users(name) VALUES(%s)""", (username))

    connection.autocommit=True
    connection.close()

    return username

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")