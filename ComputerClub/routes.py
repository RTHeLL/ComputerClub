from flask import render_template

from ComputerClub import app

from database.controller import NewsController

news_controller = NewsController()


# Index page
@app.route('/')
def main():
    return render_template('index.html', title='test', _news=news_controller.get_news())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
