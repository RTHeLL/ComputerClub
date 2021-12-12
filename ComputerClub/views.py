from flask import render_template

from ComputerClub import app

# from models import News


# Index page
@app.route('/')
def main():
    # _news = News.query.all()
    return render_template('index.html', title='test')


# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('ucp/login.html', title='Sign In', form=form)


# @app.route('/register')
