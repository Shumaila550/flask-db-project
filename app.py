from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Flask is working ✅</h1><p>Your setup is correct.</p>"

if __name__ == "__main__":
    app.run(debug=True)
