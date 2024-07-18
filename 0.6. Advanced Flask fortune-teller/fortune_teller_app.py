from flask import Flask,render_template
import random

app = Flask(__name__,
template_folder='Templates',
static_folder ='Static')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/fortune')
def fortune():
	fortunes = ["a thrilling opportunity will soon present itself.",
"unexpected wealth is headed your way.",
"your creativity will lead to great success.",
"a new friendship will bring joy and laughter.",
"travel is in your future, opening new horizons.",
"Abdalla is going to chase you around IASA.",
"trust your instincts- they will guide you wisely.",
"a long-awaited dream will finally come true.",
"good fortune will follow you wherever you go.",
"an old problem will find a surprising resolution."]
	
	TheFortune = random.choice(fortunes)
	

	return render_template('fortune.html', TheFortune = TheFortune, space =" ")



if __name__ == '__main__':
    app.run(debug = True)
