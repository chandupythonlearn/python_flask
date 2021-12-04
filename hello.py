from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Chandra")
def hello_world1():
    return "<h1>Hello, Im Chandra</h1>"

if __name__ == "__main__":
    app.run(debug=True)
