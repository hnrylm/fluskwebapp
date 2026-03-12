from flask import Flask, render_template, request
import datetime # 選擇性：加入時間紀錄

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    if request.method == 'POST':
        name = request.form.get('user_name')
        
        # --- 新增存檔功能 ---
        if name:
            # 取得目前時間 (選擇性)
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # 開啟 log.txt 進行附加寫入
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"時間: {current_time} | 訪客: {name}\n")
            print(f"已成功保存訪客: {name}") # 在終端機顯示確認
        # -------------------
        
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
