from flask import Flask, render_template  # 記得導入 render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 改用 render_template 來讀取 HTML 檔案
    return render_template('index.html',name='Henry')

@app.route('/about')
def about():
    return '<h2>這是關於我頁面！</h2>'

@app.route('/aboutme')
def aboutme():
    return '<h2>有关我!</h2>'
if __name__ == '__main__':
    app.run(port=5000, debug=True)
