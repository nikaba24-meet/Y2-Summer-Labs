from flask import Flask, render_template, request, redirect
from flask import session 
import pyrebase



firebaseConfig = {
  "apiKey": "AIzaSyBBWf96sYJDyQZGbWjcKRAGrx3R1Yg6cVo",
  "authDomain": "auth-lab-b9e1d.firebaseapp.com",
  "projectId": "auth-lab-b9e1d",
  "storageBucket" : "auth-lab-b9e1d.appspot.com",
  "messagingSenderId": "746442603326",
  "appId": "1:746442603326:web:8503248029581def9d0a6f",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'really-secret-key'


@app.route('/', methods = ['GET', 'POST'])
def main():
  if request.method == 'POST': 
    email = request.form['email']
    password = request.form['password']
    try:

      session['user'] = auth.create_user_with_email_and_password(email, password)
      session['quotes'] = []

      return redirect('/home')

    except Exception as e:
      print(e)
      return render_template('error.html')
  else:
    return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    try:
      if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        session['user'] = auth.sign_in_with_email_and_password(email, password)
        session['quotes'] = []
        return redirect('/home')
    except Exception as e:
          print(e)
          return(render_template('error.html'))
            
    return render_template('signin.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
  try:
    if request.method == 'POST':
     quote = request.form['quote']
     session['quotes'].append(quote)
     session.modified = True
     return render_template('thanks.html',)
    else:
      if 'user' not in session:
        return redirect('/signin')
      return render_template('home.html')
  except Exception as e:
    print(e)
    return render_template('error.html')

@app.route('/thanks')
def thanks():
  return render_template('thanks.html')

@app.route('/display')
def display():
  if 'user' not in session:
        return redirect('/signin') 
  print(session['quotes'])
  allQuotes = session['quotes']
  return render_template('display.html', allQuotes = allQuotes)

@app.route('/signout')
def signout():
  try:
   session.pop('user')
   session['quotes'] = []
   auth.current_user = None
   return render_template('signin.html')
  except:
    return render_template('error.html')

if __name__ == '__main__':
  app.run(debug=True)