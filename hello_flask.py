# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap(app)

# decorator binds a function to create a URL
@app.route('/')
def hello():
	return "Hello world from Flask!"

@app.route('/mytemplate')
def t_test():
    return render_template('index.html')

# to return more than one
# use debug so you do not have to restart
@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day,'
    s3 = ' friends!'
    return s1 + s2 + s3





