from flask import Flask, render_template  # 記得導入 render_template

app = Flask(__name__)

@app.route('/index')
def home():
    # 改用 render_template 來讀取 HTML 檔案
    return render_template('index.html',name='Henry')

@app.route('/about')
def about():
    # 将个人介绍存入字典
    user_info = {
        "description": "在學Python，希望能成為前端和後端programmer。能接freelance專案，在看參考書。"
    }
    return render_template('aboutme.html', info=user_info)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
