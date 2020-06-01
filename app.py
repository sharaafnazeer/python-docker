import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!. I am Python from docker"

@app.route('/how')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run()
