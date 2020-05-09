import rest
from app import app
from flask import render_template

@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/signup/page')
def sign_up_page():
	return render_template('signup.html')
		
	
@app.route('/login/page')
def login_page():
	return render_template('login.html')
		
if __name__ == "__main__":
    app.run(port=8080)