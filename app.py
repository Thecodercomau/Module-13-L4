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
            host="remotemysql.com",
            user="Rz8hqnldk4",
            password="nd0wK03xe0",
            database="Rz8hqnldk4"
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