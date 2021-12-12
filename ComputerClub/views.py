from flask import render_template

from ComputerClub import app

from .models import News


# Index page
@app.route('/')
def main():
    _news = News.query.all()
    return render_template('index.html', title='test', _news=_news)
