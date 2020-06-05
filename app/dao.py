import pyodbc
from db_config import establish_db_con
# from werkzeug.security import check_password_hash, generate_password_hash
import logging
import random
from dao_helper import *
from db_config import *
def login(username, pwd):
	
	conn = None;
	cursor = None;
	try:


		conn, cursor = establish_db_con() 

		sql = "SELECT Username, Password FROM [User] WHERE Username=?"
		sql_where = (username)

		cursor.execute(sql, sql_where)
		row = cursor.fetchone()

		if row:
			# if check_password_hash(row[1], pwd):
			if row[1] == pwd:
				return row[0]

		return None

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()

def user_exist(email,username):
	conn = None;
	cursor = None;
	
	try:
		conn, cursor = establish_db_con() 
		
		sql = "SELECT Email FROM [User] WHERE Email=? or Username=?"
		sql_where = (email,username)
		
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		
		if row:
			return True
		return False

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()

def register(email, name, pwd, affiliation):
	conn = None;
	cursor = None;
	
	try:
		conn, cursor = establish_db_con() 
		
		sql = "INSERT INTO [User] (Username, Email, Password) VALUES(?, ?, ?)"
		# data = (name, email, generate_password_hash(pwd)[:50])
		data = (name,email,pwd)
		cursor.execute(sql, data)
		
		conn.commit()

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()

def getusers(json):
	#get all users exept you
	conn = None;
	cursor = None;
	
	try:
		Username = json['username']

		conn, cursor = establish_db_con() 

		sql = """SELECT Username FROM User
				Where Username != ?
				"""
		data = (Username)

		cursor.execute(sql, data)
		row = cursor.fetchall()
		conn.commit()
		return row
	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()

def getconferences(json):

	conn = None;
	cursor = None;
	
	try:
		Username = json['username']
		Type = json['loginas']

		conn, cursor = establish_db_con() 

		sql = """SELECT Event.EventID, [Name] FROM [Event]
				INNER JOIN Participates
				On Event.EventID = Participates.EventID AND 
				Participates.Username = ? AND Participates.Type = ?
				"""
		data = (Username,Type)

		cursor.execute(sql, data)
		row = cursor.fetchall()
		conn.commit()
		return row
	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()


def getallconferences(json):
	conn = None;
	cursor = None;
	
	try:
		# Get all conferences where you are not participating as type
		Username = json['username']
		Type = json['loginas']

		conn, cursor = establish_db_con() 

		sql = """SELECT EventID, [Name] FROM [Event]
				WHERE EventID NOT IN (SELECT EventID
				FROM Participates WHERE Username = ? AND Type = ?)"""

		data = (Username,Type)

		cursor.execute(sql, data)
		row = cursor.fetchall()
		conn.commit()
		return row
		

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()


def addparticipant(json):
	conn = None;
	cursor = None;

	try:
		Username = json['username']
		EventID = json['eventid']
		Type = json['loginas']

		conn, cursor = establish_db_con()

		sql = "INSERT INTO Participates (Username, EventID, Type) VALUES(?, ?, ?)"
		data = (Username, EventID, Type)
		cursor.execute(sql, data)

		conn.commit()

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()

def createconf(json):
	conn = None;
	cursor = None;
	
	try:
		#deadline
		ProposalDeadline = json['conferencecall']
		AbstractDeadline = json['conferencedeadlines']
		#event
		Name = json['conferencename']
		Interval = json['conferencetime']
		PcMembers = json['conferencepc']
		Section = json['conferencesections']
		#username
		Username = json['chair']

		conn, cursor = establish_db_con() 



		sql = "INSERT INTO [Deadline] (ProposalDeadline,AbstractDeadline) VALUES(?,?)"
		data = (ProposalDeadline,AbstractDeadline)
		cursor.execute(sql, data)
		conn.commit()

		DeadlineID = get_last_id(conn, cursor)

		sql = "INSERT INTO [Event] (Name,Interval,DeadlineID) VALUES(?,?,?)"
		data = (Name,Interval,DeadlineID)
		cursor.execute(sql, data)
		conn.commit()
		EventId = get_last_id(conn, cursor)

		sql = "INSERT INTO [Participates] (Username,EventId,Type) VALUES(?,?,?)"
		data = (Username,EventId,'chair')
		cursor.execute(sql, data)
		conn.commit()

		conn.commit()

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()




def upproposal(json):
	conn = None;
	cursor = None;
	
	try:

		#Unique
		Username = json['username']
		EventID = json['EventID']


		#Proposal
		Name = json['proposalname']
		Topic = json['propsaltopic']
		#Paper
		PaperInfo = json['papertext']
		#Abstract
		Title = json['abstracttitle']
		AbstractName = json['abstractname']
		Purpose = json['abstractpurpose']
		Methods = json['abstractmethods']

		conn, cursor = establish_db_con() 

		
		sql = """SELECT ProposalID, AbstractID, PaperID from Participates
				Inner join Event ON Participates.EventID = Event.EventID
				Inner join Proposal On Event.EventID = Proposal.EventID
				Where Participates.Username = ? and Event.EventID = ?
				AND Participates.Type = 'author'
				"""
		data = (Username,EventID)

		cursor.execute(sql, data)
		row = cursor.fetchone()
		conn.commit()
		if row[0] != None:
			#update Event
			ProposalID = row[0]
			AbstracID = row[1]
			PaperID = row[2]


			sql = """UPDATE Proposal
				SET [Name] = ?, Topic = ?
				WHERE ProposalId = ?;
				"""
			data = (Name,Topic,ProposalID)
			cursor.execute(sql, data)
			conn.commit()

			sql = """UPDATE Paper
				SET PaperInfo = ?
				WHERE PaperID = ?;
				"""
			data = (PaperInfo,PaperID)
			cursor.execute(sql, data)
			conn.commit()

			sql = """UPDATE Abstract
				SET Title = ?, [Name] = ?, Purpose = ?, Methods = ?
				WHERE AbstractID = ?;
				"""
			data = (Title,AbstractName,Purpose,Methods,AbstracID)
			cursor.execute(sql, data)
			conn.commit()
			return 

		sql = "INSERT INTO [Paper] (PaperInfo) VALUES(?)"
		data = (PaperInfo)
		cursor.execute(sql, data)
		conn.commit()

		PaperID = get_last_id(conn, cursor)

		sql = "INSERT INTO [Abstract] (Title,[Name],Purpose,Methods) VALUES(?,?,?,?)"
		data = (Title,AbstractName,Purpose,Methods)
		cursor.execute(sql, data)
		conn.commit()
		AbstracID = get_last_id(conn, cursor)

		sql = "INSERT INTO [Proposal] (PaperID,EventID,AbstractID,[Name],Topic) VALUES(?,?,?,?,?)"
		data = (PaperID,EventID,AbstracID,Name,Topic)
		cursor.execute(sql, data)
		conn.commit()

		conn.commit()

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()