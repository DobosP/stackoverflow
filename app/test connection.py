from flaskext.mysql import MySQL
from flask import Flask
import sqlalchemy

import pymysql

myConnection = pymysql.connect( host="192.168.0.59", user="sa", passwd="<YourStrong@Passw0rd>", db="CMS2",port=1433)

app = Flask(__name__)
app.secret_key = "secret key"

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'sa'
app.config['MYSQL_DATABASE_PASSWORD'] = '<YourStrong@Passw0rd>'
app.config['MYSQL_DATABASE_DB'] = 'CMS2'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_PORT'] = 1433
mysql.init_app(app)


print("1")
conn = mysql.connect()
print("2")
cursor = conn.cursor()


# import sqlalchemy as db

# # specify database configurations
# config = {
#     'host': 'localhost',
#     'port': 1433,
#     'user': 'sa',
#     'password': '<YourStrong@Passw0rd>',
#     'database': 'CMS2'
# }
# db_user = config.get('user')
# db_pwd = config.get('password')
# db_host = config.get('host')
# db_port = config.get('port')
# db_name = config.get('database')
# # specify connection string
# connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# # connect to database
# engine = db.create_engine(connection_str)
# connection = engine.connect()
# # # pull metadata of a table
# # metadata = db.MetaData(bind=engine)
# # metadata.reflect(only=['test_table'])

# # test_table = metadata.tables['test_table']
# # test_table

# import pyodbc

# details = {
#  'server' : 'localhost',
#  'database' : 'CMS2',
#  'username' : 'sa',
#  'password' : '<YourStrong@Passw0rd>'
#  }

# connect_string = 'DRIVER={{ODBC Driver 13 for SQL Server}};SERVER={server};PORT=1443; DATABASE={database};UID={username};PWD={password})'.format(**details)

# connection = pyodbc.connect(connect_string)
# print(connection)