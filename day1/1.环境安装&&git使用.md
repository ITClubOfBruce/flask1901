## 一、环境安装

1. 编辑器：vscode，需要提前安装的插件有：Chinese（汉化），Python（解析器）

2. Git && GitHub账号

3. 命令行增强工具Cmder  视频地址：


## 二、Git的使用

1. 查看有没有安装git：cmd中输入 git --version

2. git全局设置：

   git config --global user.name "Bruce"  

   git config --global user.email "XXX@qq.com"

3. 初始化本地仓库 git init

4. 新建 .gitignore文件 

   ```
   *.pyc
   *~
   __pycache__
   .vscode
   ```

   control + O   enter  保存    control+X 退出

#### 本地仓库和远程仓库关联

1. 检查是否已经创建了SSH密钥  cat ~/.ssh/id_rsa.pub 

2. 如果上一步显示“No such file or directory”，这说明之前你没有生成过这个ssh密钥，需要先生成，使用ssh-keygen，不管提示任何东西，一路enter。

3. id_rsa 是私钥，一定不能泄露出去。id_rsa.pub是公钥，用于身份认证

4. 指定远程仓库地址  git remote add origin git@github.com:ITClubOfBruce/flaskweb.git

5. 第一次提交：

   git status  查看文件变化

   git add .   追踪文件

   git commit -m "备注"   添加到本地仓库

   git push -u origin master  第一次提交需要指定仓库，默认分支



## 三、管理环境变量

启动Flask程序时候，需要用到两个环境变量：FLASK_APP和FLASK_ENV

启动flask项目后，控制台输出：

```
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
```



  Debug mode，调试模式，设置成on，我们可以通过将FLASK_ENV设置成development来开启 

  为了不用每次启动项目都在终端中设置环境变量，我们安装用来管理系统环境变量的python--dotenv：pip install python-dotenv

  python-dotenv 默认会从项目的根目录下的.flaskenv和.env文件读取环境变量并设置，我们新建这两个文件  touch .flaskenv  .env

.flaskenv 用来存储Flask命令行系统相关的公共环境变量。 设置 FLASK_ENV=development就打开了debug mode

.env 用来存储敏感数据，不应该提交到git仓库，所以需要在.gitignore文件中设置忽略

## 四、多URL

## 五、动态URL

通过输入 http://127.0.0.1:5000/index/Bruce  ，浏览器中展示Hello，Bruce

```
# 动态URL
@app.route('/index/<name>')
def home(name):
    return "<h1>Hello，%s</h1>"%name
```

url_for函数用来生成URL:url_for('home',name="Bruce")



## 六、模板

## 七、静态文件

`<img src="{{url_for('static',filename='avatar.jpg')}}">`

在Python脚本中，需要从flask中导入url_for， 在模板里面可以直接用

static文件需要强制刷新清除缓存，之后生产环境我们会加入一个动态的版本号



## 八、数据库操作

SQLite     使用Flask-SQLAlchemy集成SQLAlchemy

1. 安装 pip install flask-sqlalchemy

2. 初始化

   ```
   from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
   app = Flask(__name__)
   db = SQLAlchemy(app)  # 初始化扩展，传入程序实例app
   ```

   

3. Flask里面，使用Flask.config接口来写入和获取设置Flask，扩展或者是程序本身的行为配置，配置变量的名称必须大写，写入配置的语句一般会放到扩展类实例化语句之前

4. 创建数据库模型

   ```
   # models
   class User(db.Model):
       id = db.Column(db.Integer,primary_key=True)
       name = db.Column(db.String(20))
   class Movie(db.Model):
       id = db.Column(db.Integer,primary_key=True)
       title = db.Column(db.String(60))
       year = db.Column(db.String(4))
   ```

   

5. 创建表和数据库文件

   ```
   进入flask shell
   >>> from app import db
   >>> db.create_all()
   >>> 
   ```

   如果改动了模型类，想重新生成表模式，需要先db.drop_all()删除表，然后在创建。

   将来使用Flask-Migrate扩展

6. 自定义数据库创建和删除的命令

   flask initdb  创建数据库

   flask initdb --drop   删除表后再创建  

7. 增删改查

   添加

   ```
   >>> from app import User,Movie
   >>> user = User(name="Bruce")  创建记录
   >>> movie1 = Movie(title="杀破狼",year="2000")
   >>> movie2 = Movie(title="战狼",year="2016")
   >>> db.session.add(user) 添加到数据库会话，只是将改动添加到一个临时区域
   >>> from app import db
   >>> db.session.add(user)
   >>> db.session.add(movie1)
   >>> db.session.add(movie2)
   >>> db.session.commit() 提交数据库会话，只需要最后调用一次
   ```

   查（读取）

   模型类.query.<过滤方法>.<查询方法>

   Movie.query.first()

   | 过滤方法    | 作用                                       |
   | ----------- | ------------------------------------------ |
   | filter()    | 筛选指定规则过滤记录，返回新产生的查询对象 |
   | filter_by() |                                            |
   | order_by()  |                                            |
   | group_by()  |                                            |

   | 查询方法       | 作用 |
   | -------------- | ---- |
   | all()          |      |
   | first()        |      |
   | get(id)        |      |
   | count()        |      |
   | first_or_404() |      |
   | get_or_404(id) |      |
   | pagination     |      |

   更新（update）

   ```
   >>> movie = Movie.query.first()
   >>> movie.title
   '杀破狼'
   >>> movie.title = "shapolang"
   >>> db.session.commit()
   ```

​       删除（delete）

```
>>> db.session.delete(movie)
>>> db.session.commit()
```



8. 在项目中操作数据库

9. 创建数据库中的数据

   

## 九、模板和代码优化



1. 错误处理函数

   ```
   @app.errorhandler(404)
   def page_not_found(e):
       user = User.query.first()
       # 返回模板和状态码
       return render_template('404.html',user=user),404
   ```

2. 模板上下文处理函数

   ```
   # 模板上下文处理函数
   @app.context_processor
   def common_user():
       user = User.query.first()
       return dict(user=user)
   ```

   返回的变量会统一注入到每一个模板的上下文环境中，所以可以直接在模板中使用

   

3. 模板继承

4. 添加百度视频链接

   ```
   <span class="float-right">
               <a class="baidu" href="http://v.baidu.com/v?word={{ movie.title }}&ct=301989888&rn=67&pn=0&db=0&s=0&fbl=800&ie=utf-8" target="_blank" title="在百度视频中查找">百度视频</a>
           </span>
   ```

   



## 十、表单

1. 表单

2. 处理表单数据

   ```
   405
   Method Not Allowed
   The method is not allowed for the requested URL.
   ```

   原因：默认处理地址请求的index视图函数默认只能接受GET请求

   ```
   @app.route('/',methods=['GET','POST'])
   ```

   

3. 针对GET和POST方法的请求，要有不同的处理逻辑

   GET：返回渲染的页面

   POST：获取表单数据并保存

   [^flask中的提醒]: flash

4. 错误信息： The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.

   flash()函数内部会把消息存储到Flask提供的session对象里。session用来在请求间存储数据，它会把数据签名后存储到浏览器的Cookie中，所以我们需要设置签名所需的密钥

   ```
   app.config['SECRET_KEY'] = 'watchlist_dev'
   ```

   这个密钥在开发时候随便设置，但是考虑的安全性，在部署时候应该设置为随机字符串，也不能明文的写到代码

5. 在模板中显示flash提示

   get_flashed_messages()  返回是一个list类型，栈
   
   



## 十一、用户认证

1. Flask 依赖的Werkzeug内置了用于生成和验证密码hash值的函数

   werkzeug.security.generate_password_hash()  生成密码

   werkzeug.security.check_password_hash()   检查密码

   ```
   >>> from werkzeug.security import generate_password_hash,check_password_hash
   >>> pw_hash = generate_password_hash('123456')
   'pbkdf2:sha256:150000$AM0Iq4hT$c0ad2c0b5c6dfb28ac092fc3ff8f12e3315f9b97263fa7e321d1a2dc31fd61c0'
   >>> check_password_hash(pw_hash,'123456')
   True
   >>> check_password_hash(pw_hash,'12345678')
   False
   ```

2. 登录登出 Flask-Login

   安装 pip install flask-login

   初始化

   ```
   from flask_login import LoginManager
   app = Flask(__name__)
   login_manager = LoginManager(app) # 实例化登录拓展类
   
   @login_manager.user_loader
   def load_user(user_id):
       user = User.query.get(int(user_id))
       return user
   ```

   current_user是Flask-Login提供的变量，如果用户已经登录，current_user变量的值就是当前用户

   让User继承Flask-Login提供的UserMixin类，继承之后User类多了几个属性，

   is_authenticated属性：如果当前用户已经登录，那么current_user.is_authenticated 会返回True，否则就是False

3. 认证保护

   @login_required





































