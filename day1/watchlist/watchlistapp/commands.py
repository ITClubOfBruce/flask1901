from watchlistapp import app,db
from watchlistapp.models import User,Movie
import click
# 自定义命令

# 新建data.db的数据库初始化命令
@app.cli.command()  # 装饰器，注册命令
@click.option('--drop',is_flag=True,help="删除后再创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成")

# 向data.db中写入数据的命令
@app.cli.command()
def forge():
    name = "Bruce"
    movies = [
        {"title":"大赢家","year":"2020"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼","year":"2020"},
        {"title":"心花路放","year":"2018"},
        {"title":"速度与激情8","year":"2012"},
        {"title":"我的父亲母亲","year":"1995"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼","year":"2020"},
        {"title":"心花路放","year":"2018"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼","year":"2020"},
        {"title":"心花路放","year":"2018"}
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo("插入数据完成")
    
# 生成管理员账号
@app.cli.command()
@click.option('--username',prompt=True,help='管理员账号')
@click.option('--password',prompt=True,help='管理员密码',hide_input=True,confirmation_prompt=True)
def admin(username,password):
    user = User.query.first()
    if user is not None:
        click.echo('更新用户信息')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建用户信息')
        user = User(username=username,name='Admin')
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo('管理员创建完成')
