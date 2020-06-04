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

# chair
@app.route("/chair")
def chair_page():
	return render_template("logged/chair/loggedchair.htm")

@app.route("/chair/createconf")
def createconf_page():
	return render_template("logged/chair/createpage/createpage.htm")

@app.route("/chair/editconf")
def editconf_page():
	return render_template("logged/chair/createpage/editpage/editpage.htm")

@app.route("/chair/selectedconf")
def selectedconf_page():
	return render_template("logged/chair/chosenconference/chosenconference.htm")

#pcmember
@app.route("/pcmember")
def pcmember_page():
	return render_template("logged/pc/loggedpc.htm")

@app.route("/pcmember/selectedconf")
def pcmember_selectedconf_page():
	return render_template("logged/pc/conferenceselected/conferenceselected.htm")

@app.route("/pcmember/selectedprop")
def pcmember_selectedprop_page():
	return render_template("logged/pc/conferenceselected/proposalselected/proposalselected.htm")

#author
@app.route("/author")
def author_page():
	return render_template("logged/author/loggedauthor.htm")

@app.route("/author/acceptedconf")
def author_acceptedconf_page():
	return render_template("logged/author/conferences_accepted/conferences_accepted.htm")

@app.route("/author/submitpaper")
def author_submitpaper_page():
	return render_template("logged/author/submit_paper/submitpaper.htm")

#listener
@app.route("/listener")
def listener_page():
	return render_template("logged/listener/loggedlistener.htm")

@app.route("/listener/details")
def listener_details_page():
	return render_template("logged/listener/paid/details.htm")

@app.route("/listener/paid")
def listener_paid_page():
	return render_template("logged/listener/paid/paid.htm")

@app.route("/listener/details_selected")
def listener_detailsselected_page():
	return render_template("logged/listener/paid/detailsselected/detailsselected.htm")

@app.route("/listener/paid_selected")
def listener_paidselected_page():
	return render_template("logged/listener/paid/paidselected/paidselected.htm")



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