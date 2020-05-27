import rest
from app import app
from os.path import dirname
from flask import render_template
from dotenv import load_dotenv
dotenv_path = f"{dirname(__file__)}\.env"  # Path to .env file
load_dotenv(dotenv_path)

# @app.route('/')
# def home_page():
# 	return render_template('index.html')

@app.route("/")
def home_page():
	return render_template("gui.htm")


@app.route("/chair")
def chair_page():
	return render_template("logged/chair/loggedchair.htm")

@app.route("/chair/createconf")
def createconf_page():
	return render_template("logged/chair/createpage/createpage.htm")

@app.route("/chair/editconf")
def editconf_page():
	return render_template("logged/chair/createpage/editpage/editpage.htm")



@app.route('/signup/page')
def sign_up_page():
	return render_template('signup.htm')

@app.route('/nav')
def nav_bar():
	return render_template('nav.htm')
		
	
@app.route('/login/page')
def login_page():
	return render_template('login.htm')
		
if __name__ == "__main__":
    app.run(port=8080,debug=True,threaded=True)