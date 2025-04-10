import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Congratulations, it's a web app!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host= "0.0.0.0", port=port)
