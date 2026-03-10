from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Localhost via Cloudflare!</h1><p>Your Flask app is now live.</p>'

if __name__ == '__main__':
    # Flask will run on http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=5000, debug=True)
