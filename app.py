from flask import Flask

app = Flask(__name__)

API_KEY = "sk_test_ABC1234567890SECRET"

@app.route("/")

def home():
    return "Welcome to the API! Your API key is: " + API_KEY
if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)