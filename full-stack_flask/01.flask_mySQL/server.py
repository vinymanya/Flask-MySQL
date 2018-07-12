from flask import Flask
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, 'mydb')

# An example of running sql query
print mysql.query_db("SELECT * FROM users LIMIT 5")

app.run(debug=True)
