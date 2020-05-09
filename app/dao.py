import pymysql
from db_config import mysql
from werkzeug.security import check_password_hash, check_password_hash
import logging

def login(email, pwd):
	
	conn = None;
	cursor = None;
	
	
	try:


		conn = mysql.connect()
		cursor = conn.cursor()
		logging.warning('Watch out!')  # will print a message to the console

		sql = "SELECT Email, Password FROM User WHERE Email=%s"
		sql_where = (email,)
		logging.warning('Watch out!')  # will print a message to the console

		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		logging.warning('Watch out!')  # will print a message to the console

		if row:
			if check_password_hash(row[1], pwd):
				return row[0]

		return None

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()

def user_exist(email):
	conn = None;
	cursor = None;
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		
		sql = "SELECT Email FROM User WHERE Email=%s"
		sql_where = (email,)
		
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

def register(email, name, pwd):
	conn = None;
	cursor = None;
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		
		sql = "INSERT INTO User(Username, Email, Password) VALUES(%s, %s, %s)"
		data = (name, email, generate_password_hash(pwd),)
		
		cursor.execute(sql, data)
		
		conn.commit()

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()