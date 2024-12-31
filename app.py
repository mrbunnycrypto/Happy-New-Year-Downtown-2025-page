from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.now().year
    if current_year == 2025:
        return "<h1>Happy New Year Downtown 2025!</h1>"
    else:
        return "<h1>Welcome to the Downtown New Year Celebration!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
