# 导入flask
from flask import Flask
import os

app = Flask(__name__)

@app.route('/') # 这个装饰器创建了home route

def home():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6000))
    app.run(debug=True, host='0.0.0.0', port=port)
