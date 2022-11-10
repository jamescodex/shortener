import string
import random
from flask import Flask, jsonify, request, abort, redirect
from faunadb import query as q
from faunadb.client import FaunaClient

app = Flask(__name__)
client = FaunaClient(secret="your-secret-here", domain="db.us.fauna.com", scheme="https")
# there are other options of region to use for your domain

def generate_identifier(n=6):
    identifier = ""
    for i in range(n):
        identifier += random.choice(string.ascii_letters)
    return identifier


@app.route("/")
def home():
    return "Hello World!"


@app.route("/generate/<path:address>/")
def generate(address):
    identifier = generate_identifier()
    if not (address.startswith("http://") or address.startswith("https://")):
        address = "http://" + address

    client.query(q.create(q.collection("urls"), {
        "data": {
            "identifier": identifier,
            "url": address
        }
    }))

    shortened_url = request.host_url + identifier
    return jsonify({"identifier": identifier, "shortened_url": shortened_url})


if __name__ == "__main__":
    app.run(debug=True)
