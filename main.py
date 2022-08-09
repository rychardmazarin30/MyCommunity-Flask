from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Clube de regatas do Flamengo</h1>"

if __name__ == "main":
    app.run()