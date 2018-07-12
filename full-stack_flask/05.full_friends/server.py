from flask import Flask, render_template, session, redirect, flash, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'fullFriendsdb')
app.secret_key = "U12Zr47j/yXR~X@Hu0|q/9!jmM]Lwf/?KTW%"

@app.route("/")
def index():
	# display all friends here
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template("index.html", all_friends=friends)

@app.route("/friends", methods=["POST"])
def create_friend():
	# add friend in the database upon form submission
	query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW() )"
	data = {
		'first_name': request.form['first_name'],
		"last_name": request.form['last_name'],
		"email": request.form['email']
	}
	mysql.query_db(query, data)
	return redirect("/")

@app.route("/friends/<friend_id>/edit")
def update(friend_id):
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
	data = { 
	"first_name": request.form['first_name'],
	"last_name": request.form['last_name'],
	"email": request.form['email'],
	"id": friend_id
	}
	update_friend = mysql.query_db(query, data)
	return render_template("update.html", updates = update_friend )


@app.route("/friends/<new_id>")
def update_redirect(new_id):
	query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :id, :email, NOW(), NOW())"
	data = {
		"first_name": request.form['first_name'],
		"last_name": request.form['last_name'],
		"email": request.form['email'],
		"id": new_id
	}
	mysql.query_db(query, data)
	return redirect("/")

@app.route("/friends/<friend_id>/delete")
def delete(friend_id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {
		"id": friend_id
	}
	mysql.query_db(query, data)
	return redirect("/")

app.run(debug=True)