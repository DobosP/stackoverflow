import pyodbc
from db_config import establish_db_con
# from werkzeug.security import check_password_hash, generate_password_hash
import logging
import random
from datetime import datetime


def get_last_id(conn, cursor):
    try:
       
        sql = "select @@IDENTITY"
        cursor.execute(sql)
        row = cursor.fetchone()
        seed_id = row[0]
        conn.commit()
        return seed_id
    except Exception as e:
        
        return None
   
