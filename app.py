
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/delete')
def assignments():
    return render_template('delete.html')


@app.route('/edit')
def contact():
    return render_template('edit.html')


@app.route('/history')
def assignments():
    return render_template('History.html')


@app.route('/index')
def assignments():
    return render_template('index.html')


@app.route('/login')
def assignments():
    return render_template('login.html')


@app.route('/register')
def assignments():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
