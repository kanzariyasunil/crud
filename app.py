from flask import Flask
from database import make_db_call
app = Flask(__name__)

@app.route('/')
def index():
    return "Hiii"

if __name__ == "__main__":
    app.run(debug=True)