from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = "Bruce"
    movies = [
        {"title":"大赢家","year":"2020"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼","year":"2020"},
        {"title":"心花路放","year":"2018"},
        {"title":"速度与激情8","year":"2012"},
        {"title":"我的父亲母亲","year":"1995"}
    ]
    return render_template('index.html',name=name,movies=movies)

