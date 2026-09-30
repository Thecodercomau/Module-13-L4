from flask import Flask, render_template, request
import mysql.connector
import re

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
            host="localhost",
            user="flaskuser",
            password="YourStrongPassword123",
            database="flask_login"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name = %s and Password = %s", (username, password))
        account = mycursor.fetchone()
        if account:
            print("Login Completed Sucessfully")
            name = account[1]
            id = [0]
            msg = "Logged In has been completed successfully"
            return render_template('index.html', msg=msg, name=name, id=id)
        else:
            msg = "Login has failed, Kindly check if you misplaced anything in the credentials"
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    name = ''
    id = ''
    msg = 'Logged out Successfully'
    return render_template('login.html', msg=msg, name=name, id=id)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and username in request.form and password in request.form and email in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        mydb = mysql.connector.connect(
            host="localhost",
            user="flaskuser",
            password="YourStrongPassword123",
            database="flask_login"
        )
        mycursor = mydb.cursor()
        print(username)
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name = %s and Password = %s", (username, password))
        account = mycursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exsists! Try Signing in'
        elif not re.match(r'^[^\d]*@[^\d]*\.\.[^\d]*$', email):
            msg = 'Oops! Your email adress is Invalid. Try Again'
        elif not re.match(r'(A-Za-z0-9)+', username):
            msg = 'Username only allows characters and numbers! Try Again.'
        elif not username or not password or not email:
            msg = 'You must fill in all the details!'
        else:
            mycursor.execute('INSERT INTO LoginDetails VALUES (%s, %s, %s)', (username, password, email))
            mydb.commit()
            msg = 'Your registration has been completed and will be redirected shortly'
            name = username
            return render_template('index.html', msg=msg, name=name)
    elif request.method == 'POST':
        msg = 'You must fill the details! Registration Unsuccessful'
        return render_template('registration.html', msg=msg) 


@app.route('/', methods=['GET', 'POST'])

def index():

    return render_template('login.html')

app.run(host='0.0.0.0', port=8080)
