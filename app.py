import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Bienvenu!"

@app.route('/comment allez vous')
def salut():
    return 'Je vais bien et toi?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
