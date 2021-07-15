from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! I know it works if I write this. I also know that it is the Flask version. \n This is for Deploy."
