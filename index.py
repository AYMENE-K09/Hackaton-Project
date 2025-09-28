from flask import Flask

app = Flask(__name__)

@app.rout('/')
def home():
    return "Hello, Library"

if __name__=="__main__":
    app.run(debug=True)
