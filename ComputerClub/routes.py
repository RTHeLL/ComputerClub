from flask import render_template

from ComputerClub import app

from database.controller import NewsController

news_controller = NewsController()


# Index page
@app.route('/')
def main():
    return render_template('index.html', title='test', _news=news_controller.get_news())
