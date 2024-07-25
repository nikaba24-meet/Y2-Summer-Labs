from flask import Flask,render_template, url_for, redirect,request
from flask import session
from datetime import date
from datetime import timedelta
import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyBdZInsQXCh1E3zx81jrsyQQ1wh0Ovgsq4",
  "authDomain": "mood-tracking-website.firebaseapp.com",
  "databaseURL": "https://mood-tracking-website-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "mood-tracking-website",
  "storageBucket": "mood-tracking-website.appspot.com",
  "messagingSenderId": "631957659536",
  "appId": "1:631957659536:web:5210862726fbe2717f1d15"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db =firebase.database()


app = Flask(__name__,
template_folder='templates',
static_folder ='static')

app.config['SECRET_KEY'] = "My_secret_string"

#what is the date
today = date.today()
Date = today.strftime("%B %d %Y") 
cDate = Date.split()
cMonth = cDate[0]
cDay = cDate[1]
yesterday = today - timedelta(days = 1)

#sign in route - main route

@app.route('/' , methods= ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = {
                'email': email}
            session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for(('today')))
        except Exception as e:
            print(e)
            return render_template('signin.html')
    else:
        return render_template('signin.html')

#sign up route 

@app.route('/signup', methods= ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = {
                'email': email,
                }
            session['user'] = auth.create_user_with_email_and_password(email, password)
            db.child('Users').child(session['user']['localId']).set(user)
            return render_template('today.html')
        except Exception as e:
            print(e)
            return render_template('signup.html')
    else:
        return render_template('signup.html')

# today route 

@app.route('/today', methods = ['GET', 'POST'])
def today():
	user_exists = (db.child('moodPosts').child(session['user']['localId']).get().val() != None)
	if (user_exists and not Date in db.child('moodPosts').child(session['user']['localId']).get().val()) or (not user_exists):
		if request.method == 'POST':
			umood = request.form['mood']
			uhobbies = request.form['hobbies']
			uother = request.form['other']
			generalDay = {
				'umood': umood,
				'uhobbies': uhobbies,
				'uother': uother
				}
			print(generalDay)
			db.child('moodPosts').child(session['user']['localId']).child(Date).set(generalDay)
			if umood == 'happy' or umood == 'energetic':
				todayMood = 'good ♡〜٩( ˃▿˂ )۶〜♡'
			else: 
				todayMood = 'bad ૮₍´˶• . • ⑅ ₎ა'
			return render_template('todaySummary.html', todayMood = todayMood)
		else:
			return render_template('today.html')
	else:
		moods = db.child('moodPosts').child(session['user']['localId']).child(Date).get().val()
		return render_template("todayAlready.html", umood = moods['umood'], uhobbies = moods['uhobbies'], uother = moods['uother'])
		
@app.route('/yesterday', methods = ['GET', 'POST'])
def yesterday():
	yesterdayLog = db.child('moodPosts').child(session['user']['localId']).child(yesterday).get().val() != None
	if yesterdayLog == True:
		ymoods = db.child('moodPosts').child(session['user']['localId']).child(yesterday).get().val()
		return render_template('yesterdayLogged.html', umood = ymoods['umood'], uhobbies = ymoods['uhobbies'], uother = ymoods['uother'])
	else: 
		return render_template('yesterdayNo.html')
	
@app.route('/tomorrow')
def tomorrow():
	return render_template('tomorrow.html')
#I'm not using this anymore
@app.route('/calendar', methods = ['GET','POST'])
def calendar():
	return render_template('calendar.html')

@app.route('/signout')
def signout():
  session.pop('user')
  auth.current_user = None
  return redirect('/')


if __name__ == '__main__':
  app.run(debug=True)