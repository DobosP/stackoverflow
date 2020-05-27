import pyodbc
from db_config import establish_db_con
# from werkzeug.security import check_password_hash, generate_password_hash
import logging
import random
from datetime import datetime


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



def getconferences():
	conn = None;
	cursor = None;
	
	try:

		conn, cursor = establish_db_con() 

		sql = "SELECT Interval FROM [Event]"
		sql_where = ()

		cursor.execute(sql, sql_where)
		row = cursor.fetchone()

		return row
		

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
		conn, cursor = establish_db_con() 
		random.seed(datetime.now())
		sql = "INSERT INTO [Event] (EventID,Interval) VALUES(?,?)"
		# data = (name, email, generate_password_hash(pwd)[:50])
		data = (random.randint(1,100),json['conferencename'])
		cursor.execute(sql, data)

		conn.commit()

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()