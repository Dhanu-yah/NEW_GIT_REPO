from flask import Flask
app = Flask(__name__)

@app.route("/")

def home():
    return "HELLO FROM DOCKER! TODAY IS MONDAY THE DAYE IS 26 OCTOBER 2026"
app.run(host="0.0.0.0", port=5005)
