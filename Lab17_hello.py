from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Task 2: Hello World
@app.route('/')
def hello():
	return "Hello world from Flask!"

# Task 3: Adding Templates
@app.route('/woodward')
def t_test():
	return render_template('template.html')




