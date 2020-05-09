from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'sa'
app.config['MYSQL_DATABASE_PASSWORD'] = '<YourStrong@Passw0rd>'
app.config['MYSQL_DATABASE_DB'] = 'CMS2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 1433
mysql.init_app(app)