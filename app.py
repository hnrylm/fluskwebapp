from flask import Flask, render_template, request # 這裡要多引入 request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])      # 根目錄支援 GET 和 POST
@app.route('/index', methods=['GET', 'POST']) # /index 也支援 GET 和 POST
def index():
    user_name = "Henry" # 預設名字
    
    if request.method == 'POST':
        # 從表單內部 (POST) 拿數據
        user_name = request.form.get('name', 'Henry')
    else:
        # 如果是普通訪問 (GET)，從網址參數拿數據
        user_name = request.args.get('name', 'Henry')
        
    return render_template('index.html', name=user_name)

# @app.route('/')
# def home():
#     # 改用 render_template 來讀取 HTML 檔案
#     return render_template('index.html',name='Henry')



@app.route('/about')
def about():
    # 将个人介绍存入字典
    user_info = {
        "description": "在學Python，希望能成為前端和後端programmer。能接freelance專案，在看參考書。"
    }
    return render_template('aboutme.html', info=user_info)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
