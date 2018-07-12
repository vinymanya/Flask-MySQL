from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, "restful-usersDB")

app.secret_key = "wtuiyiruiguogioigp"
EMAIL_REGX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')



@app.route("/users")
def index():
	# Retrieve all users from db
	query = "SELECT users.id, CONCAT(users.first_name, ' ', users.last_name) AS full_name, users.email AS email, users.created_at AS time_stamp FROM users"
	users = mysql.query_db(query)
	return render_template("index.html", users=users)

@app.route("/")
def wild_card():
	return redirect(url_for("index"))

# Display a form to allow users to add a new user in the list
@app.route("/users/new")
def add_user():
	return render_template("new.html")

# Create users
@app.route("/users/create", methods=["POST"])
def create_user():
	errors = []
	first_name = request.form["first_name"]
	last_name = request.form["last_name"]
	email = request.form["email"]
	# Validate form
	if len(first_name) < 1:
		errors.append("First Name cannot be empty!")
	if len(last_name) < 1:
		errors.append("Last Name cannot be empty!")
	if not EMAIL_REGX.match(email):
		errors.append("Invalid email address!")

	# Check if there are any errors
	if len(errors) > 0:
		for message in errors:
			flash(message)
			return redirect(url_for("add_user"))

	
	# Insert into db and redirect home
	query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) VALUES(:fn, :ln, :email, NOW(), NOW())"
	data = {
		"fn": request.form["first_name"],
		"ln": request.form["last_name"],
		"email": request.form["email"]
	}
	mysql.query_db(query, data)
	return redirect(url_for("index"))


# Show a particular user
@app.route("/users/<user_id>")
def show(user_id):
	# Get a single user from db
	query = "SELECT users.id AS user_id, CONCAT(users.first_name, ' ', users.last_name) AS full_name, users.email AS email, users.created_at AS time_stamp FROM users WHERE id = :user_id"
	data = {
		"user_id": user_id
	}
	one_user = mysql.query_db(query, data)
	return render_template("show.html", user=one_user)

# Delete a particular user
@app.route("/users/<user_id>/delete")
def destroy(user_id):
	# Get a single user from db
	query = "DELETE FROM users WHERE id = :user_id"
	data = {
		"user_id": user_id
	}
	mysql.query_db(query, data)
	return redirect(url_for("index"))

# Edit a particular user
@app.route("/users/<user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
	# Store the id from the URL
	url_id = user_id

	if request.method == "GET":
		# Retrieve a single user
		query = "SELECT * FROM users WHERE id = :user_id"
		data = {
			"user_id": user_id
		}
		one_user = mysql.query_db(query, data)
		return render_template("edit.html", user=one_user, _id=url_id)
	
	# Make sure to validate inputs
	errors = []
	first_name = request.form["first_name"]
	last_name = request.form["last_name"]
	email = request.form["email"]
	# Validate form
	if len(first_name) < 1:
		errors.append("First Name cannot be empty!")
	if len(last_name) < 1:
		errors.append("Last Name cannot be empty!")
	if not EMAIL_REGX.match(email):
		errors.append("Invalid email address!")

	# Check if there are any errors
	if len(errors) > 0:
		for message in errors:
			flash(message)
			# Construct the URL with id above to redirect to the same page
			return redirect("/users/{}/edit".format(url_id))
	# Update user in db
	query = "UPDATE users set first_name = :fn, last_name = :ln, email = :email, created_at = NOW(), updated_at = NOW() WHERE id=:user_id"
	data = {
		"fn": first_name,
		"ln": last_name,
		"email": email,
		"user_id": user_id
	}
	mysql.query_db(query, data)
	return redirect("/users/{}".format(url_id))

app.run(debug=True)