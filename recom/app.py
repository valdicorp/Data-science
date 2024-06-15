from flask import Flask, request, jsonify

app=Flask(__name__)
@app.route("/")

def home():
    return "salut"

if __name__=="app":
    app.run(debug=True)