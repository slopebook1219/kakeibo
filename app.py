from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask is running!"

if __name__ == "__main__":
    app.run(debug=True)


# テストコメントです
#復習中、テストコメント二号です。