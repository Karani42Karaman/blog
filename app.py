import json
from flask import Flask, render_template

app = Flask(__name__)

def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    portfolio_data = load_data()
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    # debug=True sayesinde JSON'ı değiştirdiğinde site otomatik yenilenir
    app.run(debug=True, port=5000)