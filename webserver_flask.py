from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def home():
    return 'Hello world'


@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

