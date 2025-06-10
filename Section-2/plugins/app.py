from flask import Flask
from calculator import calc_bp  # plugin import

app = Flask(__name__)
app.register_blueprint(calc_bp)  # plugin registration

@app.route("/")
def home():
    return "Welcome to Miya's Modular Math Den!"

