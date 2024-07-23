from flask import Flask,render_template, url_for, redirect,request
from flask import session
from datetime import date
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
cDate = today.strftime("%B %d %Y") 
cDate = cDate.split()
cMonth = cDate[0]
cDay = cDate[1]

#sign in route - main route

@app.route('/' , methods= ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

        try:
            user = {
                'username': username,
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
        username = request.form['username']

        try:
            user = {
                'username': username,
                'email': email,
                "cMonth": cMonth
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
	if request.method == 'POST':
		umood = request.form['mood']
		uhobbies = request.form['hobbies']
		uother = request.form['other']
		generalDay = {
			'umood': umood,
			'uhobbies': uhobbies,
			'uother': uother}
	else:
		return render_template('today.html')
	# except Exception as e:
	# 	print(e)
	#db.child('Users').child(session['user']['localId']).set()
	





if __name__ == '__main__':
  app.run(debug=True)