from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Localhost via Cloudflare!</h1><p>Your Flask app is now live.</p>'

@app.route('/about')
def about():
    return '<h2>這是我的第一個 Flask 網站！</h2><p>我正在學習如何將本地開發環境連接到雲端。</p>'

if __name__ == '__main__':
    # Flask will run on http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=5000, debug=True)
