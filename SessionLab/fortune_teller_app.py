from flask import Flask,render_template, url_for, redirect,request
import random
from flask import session

app = Flask(__name__,
template_folder='Templates',
static_folder ='Static')


app.config['SECRET_KEY'] = "My_secret_string"


@app.route('/', methods = ['GET', 'POST'])
def main():
	print('\033[92m' + "In main, " + request.method + '\033[0m')
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		print('\033[92m' + "Click, " + request.method + '\033[0m')
		userName = request.form['name']
		userBirthmonth = request.form['userBirthmonth']
		session['name_user'] = userName
		session['birthmonth_user'] = userBirthmonth 
		return redirect(url_for('home'))


@app.route('/home', methods = ['GET', 'POST'])
def home():
	print('\033[92m' + "In home, " + request.method + '\033[0m')
	if request.method == 'GET':
		return render_template('home.html')
	elif request.method == 'POST':

		return redirect(url_for('fortune'))

@app.route('/fortune')
def fortune():
	print('\033[92m' + "In fortune, " + request.method + '\033[0m')
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
	
	if len(session['birthmonth_user']) <= 10: 
		fortuneIndex = len(session['birthmonth_user'])-1
		TheFortune = fortunes[fortuneIndex]
	else:
		TheFortune = "Opportunities for growth and prosperity await you on your current path."
	

	return render_template('fortune.html', TheFortune = TheFortune)



if __name__ == '__main__':
    app.run(debug = True)
