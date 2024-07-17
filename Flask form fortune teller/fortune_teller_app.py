from flask import Flask,render_template, url_for, redirect,request
import random

app = Flask(__name__,
template_folder='Templates',
static_folder ='Static')

@app.route('/home', methods = ['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		birthmonth = request.form['birthmonth']
		return redirect(url_for('fortune', BM = birthmonth))

@app.route('/fortune <BM>')
def fortune(BM):
	fortunes = ["a thrilling opportunity will soon present itself.",
"unexpected wealth is headed your way.",
"your creativity will lead to great success.",
"a new friendship will bring joy and laughter.",
"travel is in your future, opening new horizons.",
"Abdalla is going to chase you around IASA.",
"trust your instincts; they will guide you wisely.",
"a long-awaited dream will finally come true.",
"good fortune will follow you wherever you go.",
"an old problem will find a surprising resolution."]
	
	if len(BM) <= 10: 
		fortuneIndex = len(BM)-1
		TheFortune = fortunes[fortuneIndex]
	else:
		TheFortune = "Opportunities for growth and prosperity await you on your current path."
	

	return render_template('fortune.html', TheFortune = TheFortune)



if __name__ == '__main__':
    app.run(debug = True)
