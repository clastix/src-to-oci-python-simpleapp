from os import getenv
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    hello_msg = getenv("HELLO_MSG") or "world"
    return "Hello " + hello_msg + "!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
