import dao
import json
from app import app
from logging import warning
from flask import jsonify, request, session
		

@app.route('/signup', methods=['POST'])
def signup():
	_json = request.json
	_name = _json['name']
	_email = _json['email']
	_pwd = _json['password']
	
	if _email and _name and _pwd:
	
		user_exist = dao.user_exist(_email)
		
		if user_exist == True:
			resp = jsonify({'message' : 'User already registered'})
			resp.status_code = 409
			return resp
		else:		
			dao.register(_email, _name, _pwd)
			
			resp = jsonify({'message' : 'User registered successfully'})
			resp.status_code = 201
			return resp
	else:
		resp = jsonify({'message' : 'Bad Request - invalid parameters'})
		resp.status_code = 400
		return resp

@app.route('/login', methods=['POST'])
def login():

	_json = request.json
	#print(_json)
	_username = _json['username']
	_password = _json['password']
	print("Asa se face 1")
	if _username and _password:
		user = dao.login(_username, _password)
		
		if user != None:
			session['username'] = user
			return jsonify({'message' : 'User logged in successfully'})

	resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
	resp.status_code = 400
	return resp

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username', None)
	return jsonify({'message' : 'You successfully logged out'})