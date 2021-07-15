from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! I know it works if I write this."
