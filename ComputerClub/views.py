from flask import render_template

from ComputerClub import app
from ComputerClub.forms import LoginForm


# Main page
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
