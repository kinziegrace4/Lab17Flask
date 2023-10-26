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

# Created another simple app route to add a different template using a background image and pdf link
# I wanted to get more practice on git
@app.route('/woodward/resume')
def t_test2():
	return render_template('new_template.html')



