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

		sql = """SELECT Username FROM [User]
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
		#username
		Username = json['chair']
		#EventId
		EventId = json['EventID']
		conn, cursor = establish_db_con() 


		if EventId:

			sql = """SELECT DeadlineID FROM [Event]
			WHERE EventID= ? """
			
			data = (EventId)



			sql = "UPDATE [Event] set  [Name] = ?, Interval = ? where EventID = ?"
			data = (Name,Interval,EventId)
			cursor.execute(sql, data)
			conn.commit()

			for pcmember in PcMembers:
				try:
					sql = "INSERT INTO [Participates] (Username,EventId,Type) VALUES(?,?,?)"
					data = (pcmember,EventId,'PCmember')
					cursor.execute(sql, data)
					conn.commit()
				except Exception as e:
					print(e)


			conn.commit()
			return



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
		for pcmember in PcMembers:
			try:
				sql = "INSERT INTO [Participates] (Username,EventId,Type) VALUES(?,?,?)"
				data = (pcmember,EventId,'PCmember')
				cursor.execute(sql, data)
				conn.commit()
			except Exception as e:
				print(e)


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
		Autors = json['proposalauthors']

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
		if row:
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

			for author in Autors:
				try:
					sql = "INSERT INTO [Participates] (Username,EventId,Type) VALUES(?,?,?)"
					data = (author,EventID,'author')
					cursor.execute(sql, data)
					conn.commit()
				except Exception as e:
					print(e)

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

	
		for author in Autors:
			try:
				sql = "INSERT INTO [Participates] (Username,EventId,Type) VALUES(?,?,?)"
				data = (author,EventID,'author')
				cursor.execute(sql, data)
				conn.commit()
			except Exception as e:
				print(e)

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()

def getproposalinfo(json):
	conn = None;
	cursor = None;

	try:
		Username = json['username']
		EventID = json['EventID']

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

		if row:

			sql = """SELECT Proposal.Name, Proposal.Topic, PaperInfo, Title, Abstract.Name, Purpose, Methods from Proposal
					Inner join Paper ON Proposal.PaperID = Paper.PaperID
					Inner join Abstract ON Proposal.AbstractID = Abstract.AbstractID
					Where Proposal.ProposalID = ?
					"""
			data = (row[0])

			cursor.execute(sql,data)
			row = cursor.fetchone()
			conn.commit()
			data={
				'proposalname': row[0],
				'propsaltopic': row[1],
				'papertext': row[2],
				'abstracttitle': row[3],
				'abstractname': row[4],
				'abstractpurpose': row[5],
				'abstractmethods': row[6]
			}

			return data
		else:
			return None

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()


def getallproposals(json):
	conn = None;
	cursor = None;

	try:
		# Get all proposals where you are not participating as author
		Username = json['username']
		eventID = json['EventID']

		conn, cursor = establish_db_con()

		sql = """SELECT ProposalID, [Name] FROM Proposal
				WHERE Proposal.EventId = ? AND Proposal.ProposalID NOT IN (SELECT Proposal.ProposalID
				FROM Participates inner join Event on Event.EventID = Participates.EventID
				inner join Proposal on Event.EventID = Proposal.EventId
				WHERE Participates.Username = ? AND Type = ?)"""

		data = (eventID,Username, "author")

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

def addpcmember(json):
	conn = None;
	cursor = None;

	try:
		Username = json['username']
		ProposalID = json['ProposalID']
		Analyze = json['Analyze']

		conn, cursor = establish_db_con()

		sql = "INSERT INTO PCmember (Username, ProposalID, Analyze) VALUES(?, ?, ?)"
		data = (Username, ProposalID, Analyze)
		cursor.execute(sql, data)

		conn.commit()

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()


def getallpcmembers(json):
	# get all users exept you
	conn = None;
	cursor = None;

	try:
		eventid = json['eventid']

		conn, cursor = establish_db_con()

		sql = """SELECT Username, ProposalID, Analyze FROM PCmember
				Where Username IN (SELECT Username From Participates
				where EventID = ?"""

		data = eventid
		cursor.execute(sql,data)
		row = cursor.fetchall()
		conn.commit()
		return row
	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()


def getconference(json):
	conn = None
	cursor = None

	try:
		EventID = json['EventID']

		sql = "Select * from Event Where EventID = ?"
		data=(EventID)
		conn, cursor = establish_db_con()
		cursor.execute(sql,data)
		row = cursor.fetchone()
		conn.commit()

		if row:

			sql = """SELECT [Name], Interval, ProposalDeadline,AbstractDeadline from Event
					Inner join Deadline ON Deadline.DeadlineID = Event.DeadlineID
					WHERE EventId = ?
					"""

			data = (EventID)

			cursor.execute(sql, data)
			row = cursor.fetchone()
			conn.commit()

			
			data={
				'conferencename': row[0],
				'conferencetime': row[1],
				'conferencecall': row[2],
				'conferencedeadlines': row[3]
			}

			return data
		else:
			return None


	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()
