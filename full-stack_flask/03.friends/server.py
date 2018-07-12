from flask import Flask, render_template, request, redirect, url_for
from mysqlconnection import MySQLConnector

app = Flask(__name__)
# Establish a connection with the db
mysql = MySQLConnector(app, 'mydb')

@app.route("/")
def index():
	# Display all friends
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template("index.html", all_friends= friends)


# Show one friend
@app.route("/friend/<friend_id>")
def show_friend(friend_id):
	# Show details of a single friend
	query = "SELECT * FROM friends WHERE id = :selected_id"
	data = {
		"selected_id": friend_id
	}

	friends = mysql.query_db(query, data)
	return render_template("show.html", one_friend = friends[0])

# Update a friend
@app.route("/update_friend/<friend_id>", methods=["POST"])
def update_friend(friend_id):
	# Show details of a single friend
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation, created_at = NOW(), updated_at = NOW()  WHERE id = :id"
	data = {
		"first_name": request.form["first_name"],
		"last_name": request.form["last_name"],
		"occupation": request.form["occupation"],
		"id": friend_id
	}

	friends = mysql.query_db(query, data)
	return redirect(url_for("index"))

# Delete a Friend
@app.route("/remove_friend/<friend_id>")
def remove_friend(friend_id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {
		"id": friend_id
	}
	mysql.query_db(query, data)
	return redirect(url_for("index"))


# Create a Friend
@app.route("/friends", methods=["POST"])
def create():
	# add a friend to the database
	query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES(:first_name, :last_name, :occupation, NOW(), NOW())"
	data = {
		"first_name": request.form['first_name'],
		"last_name": request.form['last_name'],
		"occupation": request.form['occupation']
	}
	mysql.query_db(query, data)
	return redirect(url_for("index"))


app.run(debug=True)