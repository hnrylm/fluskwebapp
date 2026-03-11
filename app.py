from flask import Flask, render_template, request # 這裡要多引入 request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_name = "Henry"
    if request.method == 'POST':
        user_name = request.form.get('name', 'Henry')
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"{user_name}\n") # 只存名字，方便讀取
            
    # --- 新增：讀取檔案中最後 5 個名字 ---
    try:
        with open("log.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # 取得最後 5 行，並去掉換行符號
            recent_visitors = [line.strip() for line in lines[-5:]]
    except FileNotFoundError:
        recent_visitors = []
    # ----------------------------------

    return render_template('index.html', name=user_name, visitors=recent_visitors)

@app.route('/about')
def about():
    # 将个人介绍存入字典
    user_info = {
        "description": "在學Python，希望能成為前端和後端programmer。能接freelance專案，在看參考書。"
    }
    return render_template('aboutme.html', info=user_info)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
