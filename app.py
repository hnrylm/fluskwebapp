from flask import Flask, render_template, request # 這裡要多引入 request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nname = None
    if request.method == 'POST':
        name = request.form.get('user_name')
    
    return render_template('index.html',name=name)

@app.route('/about')
def about():
    # 将个人介绍存入字典
    user_info = {
        "description": "在學Python，希望能成為前端和後端programmer。能接freelance專案，在看參考書。"
    }
    return render_template('aboutme.html', info=user_info)

if __name__ == '__main__':
    #app.run(port=5000, debug=True)
    app.run(debug=True)