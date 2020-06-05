import dao
import json
from app import app
from logging import warning
from flask import jsonify, request
		

@app.route('/signup', methods=['POST'])
def signup():
	_json = request.json
	_username = _json['username']
	_email = _json['email']
	_pwd = _json['password']
	_affiliation = _json['affiliation']
	
	if _email and _username and _pwd and _affiliation:
	
		user_exist = dao.user_exist(_email,_username)
		if user_exist == True:
			resp = jsonify({'message' : 'User already registered'})
			resp.status_code = 409
			return resp
		else:		
			dao.register(_email, _username, _pwd, _affiliation)
			
			resp = jsonify({'message' : 'User registered successfully'})
			resp.status_code = 201
			return resp
	else:
		resp = jsonify({'message' : 'Bad Request - invalid parameters'})
		resp.status_code = 400
		return resp

@app.route('/createconf', methods=['POST'])
def createconf():
	_json = request.json

	
	if _json['conferencename']:
	
	
		dao.createconf(_json)
		
		resp = jsonify({'message' : 'User registered successfully'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Bad Request - invalid parameters'})
		resp.status_code = 400
		return resp

@app.route('/upproposal', methods=['POST'])
def upproposal():
	_json = request.json
	if _json['proposalname']:
	
	
		dao.upproposal(_json)
		
		resp = jsonify({'message' : 'User registered successfully'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Bad Request - invalid parameters'})
		resp.status_code = 400
		return resp


@app.route('/getproposalinfo', methods=['GET'])
def getproposalinfo():
	get_data = {
		"username": request.args.get('username'),
		"EventID": request.args.get('EventID')
		}
	data = dao.getproposalinfo(get_data)
	if data:
		proposal = [data]
		resp = jsonify(proposal)
		resp.status_code = 200
		return resp
	else:
		resp = jsonify({'message': 'Bad Request - no proposal found'})
		resp.status_code = 404
		return resp


@app.route('/login', methods=['POST'])
def login():

	_json = request.json

	_username = _json['username']
	_password = _json['password']
	_loginas = _json['loginas']
	if _username and _password:
		user = dao.login(_username, _password)
		
		if user != None:
			# session['username'] = user
			return jsonify({'message' : f'User logged in successfully as {_loginas}'})

	resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
	resp.status_code = 400
	return resp


@app.route('/getconferences', methods=['GET'])
def getconferences():
	get_data = {
		"username": request.args.get('username'),
		"loginas":  request.args.get('loginas')
		}
	data = dao.getconferences(get_data)
	events = []
	for event in data:
		events.append({
		"EventID": event[0],
		"Name": event[1]
		})
	resp = jsonify(events)
	resp.status_code = 200

	return resp

@app.route('/getallconferences', methods=['GET'])
def getallconferences():
	get_data = {
		"username": request.args.get('username'),
		"loginas":  request.args.get('loginas')
		}
	data = dao.getallconferences(get_data)
	events = []
	for event in data:
		events.append({
		"EventID": event[0],
		"Name": event[1]
		})
	resp = jsonify(events)
	resp.status_code = 200

	return resp

@app.route('/getusers', methods=['GET'])
def getallusers():
	get_data = {
		"username": request.args.get('username'),
		}
	data = dao.getusers(get_data)
	events = []
	for event in data:
		events.append({
		"Username": event[0],
		})
	resp = jsonify(events)
	resp.status_code = 200

	return resp

@app.route('/getallproposals', methods=['GET'])
def getallproposals():
	get_data = {
		"username": request.args.get('username'),
		"EventID": request.args.get("EventID")
		}
	data = dao.getallproposals(get_data)
	events = []
	for event in data:
		events.append({
		"ProposalID": event[0],
		"Name": event[1]
		})
	resp = jsonify(events)
	resp.status_code = 200

	return resp

@app.route('/addpcmember', methods=['POST'])
def addpcmember():
	_json = request.json
	dao.addpcmember(_json)

	resp = jsonify({'message': 'PCmember added successfully'})
	resp.status_code = 201
	return resp

@app.route('/getallpcmembers', methods=['GET'])
def getallpcmemberss():
	get_data = {
		"event": request.args.get('eventid'),
		}
	data = dao.getallproposals(get_data)
	pcmembers = []
	for pcmember in data:
		pcmember.append({
		"Username": pcmembers[0],
		"ProposalID": pcmembers[1],
		"Analyze": pcmembers[2]
		})
	resp = jsonify(events)
	resp.status_code = 200

	return resp


@app.route('/addparticipant', methods=['POST'])
def addparticipant():
	_json = request.json
	warning(_json)
	dao.addparticipant(_json)
	resp = jsonify({'message': 'Participant added successfully'})
	resp.status_code = 201
	return resp

# @app.route('/logout', username)
# def logout():
# 	_json = request.json

# 	_username = _json['username']
# 	if 'username' in session:
# 		session.pop('username', None)
# 	return jsonify({'message' : 'You successfully logged out'})