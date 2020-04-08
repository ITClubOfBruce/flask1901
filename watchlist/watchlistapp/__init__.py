import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
from flask_login import LoginManager

app = Flask(__name__)
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path),'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'watchlist_dev'

db = SQLAlchemy(app)  # 初始化扩展，传入程序实例app


login_manager = LoginManager(app) # 实例化登录拓展类

@login_manager.user_loader
def load_user(user_id):
    from watchlistapp.models import User
    user = User.query.get(int(user_id))
    return user
login_manager.login_view = 'login'


# 模板上下文处理函数
@app.context_processor
def common_user():
    from watchlistapp.models import User
    user = User.query.first()
    return dict(user=user)

from watchlistapp import views,errors,commands