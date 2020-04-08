from backend import run
from flask_wtf.csrf import generate_csrf

app = run.create_app()

@app.after_request
def after_request(response):
    # 调用函数生成csrf token
    csrf_token = generate_csrf()
    print(csrf_token)
    # 设置cookie传给前端
    response.set_cookie('csrf_token', csrf_token)
    return response