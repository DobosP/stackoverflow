import pyodbc

server = 'localhost'
database = 'CMS2'
username = 'sa'
password = 'password'
driver = '{ODBC Driver 17 for SQL Server}'

connectionstring = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def establish_db_con():

    sql_con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = sql_con.cursor()
   
    return sql_con, cursor