from flask import Flask, render_template, request # 這裡要多引入 request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])      # 根目錄支援 GET 和 POST

@app.route('/index', methods=['GET', 'POST'])
def index():
        user_name = "Henry" 
        
        if request.method == 'POST':
            user_name = request.form.get('name', 'Henry')
            # --- 核心修復：寫入檔案必須放在 return 之前，且要有縮進 ---
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"新訪客: {user_name}\n")
            # -----------------------------------------------------
        else:
            user_name = request.args.get('name', 'Henry')
            
        return render_template('index.html', name=user_name)


@app.route('/about')
def about():
    # 将个人介绍存入字典
    user_info = {
        "description": "在學Python，希望能成為前端和後端programmer。能接freelance專案，在看參考書。"
    }
    return render_template('aboutme.html', info=user_info)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
