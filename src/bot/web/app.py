from flask import Flask


app = Flask(__name__)


@app.route("/")
def root() -> str:
    return "Hello, world!"


def run() -> None:
    app.run("0.0.0.0", port=8080)
