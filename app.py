import string
import random
from flask import Flask, jsonify, request, abort, redirect
from faunadb import query as q
from faunadb.client import FaunaClient

app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)
