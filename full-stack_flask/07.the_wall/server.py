from flask import Flask, render_template, request,redirect, flash, session, url_for
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
from functools import wraps
import re

app = Flask(__name__)
app.secret_key = "W12Zr47j/3yX R~X@Hu0|q/9!jmM]Lwf/,?KTW%"
EMAIL_REGX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app, "walldb")
bcrypt = Bcrypt(app)

@app.route("/")
def index():
	# Check to see if the user is logged in or not
	if "user_id" in session:
		return redirect(url_for("dashboard"))
	#just render template: the login and the Registration form
	return render_template("index.html")

@app.route("/users/register", methods=["POST"])
def register():
	# validation process
	errors = []
	if len(request.form["first_name"]) < 1:
		errors.append("First Name cannot be empty! and it must be at least 2 characters long!")
	if len(request.form["last_name"]) < 1:
		errors.append("Last Name cannot be empty and it must be at least 2 characters long!")
	if not EMAIL_REGX.match(request.form["email"]):
		errors.append("Invalid email address!")
	if len(request.form["password"]) < 6:
		errors.append("password must be at leat 6 characters!!!")
	if request.form["password"] != request.form["pw_con"]:
		errors.append("Passwords don't match!!!")
	# Check if there are errors
	if len(errors) > 0:
		for message in errors:
			flash(message, "error")
			return redirect(url_for("index"))
	else:
		# Preventing users from registering multiple time with the same email:
		query_email = "SELECT * FROM users WHERE email = :email"
		data = {
			"email": request.form["email"]
		}
		user = mysql.query_db(query_email, data) #[], [{}]
		if user:
			flash("Invalid email or password!", "error")
			return redirect("/")
		# Then if there is no user with that email, go ahead and encrypt the password
		else:
			password = request.form["password"]
			pw_hash = bcrypt.generate_password_hash(password)
		# Database insertion
			query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:fn, :ln, :email, :pw, NOW(), NOW())"
			data = {
				"fn": request.form["first_name"],
				"ln": request.form["last_name"],
				"email": request.form["email"],
				"pw": pw_hash
			}
			user1 = mysql.query_db(query, data)

			# keeping track of the user:
			query = "SELECT users.id, users.first_name FROM users WHERE id =:id"
			data = {
				"id": user1
			}
			user = mysql.query_db(query, data)
			# Save the user in session
			session["user_id"] = user[0]["id"]
			session["user_name"] = user[0]["first_name"]
			flash("You have successfully registered !", "success")
			return redirect(url_for('dashboard'))


@app.route("/users/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		username = request.form["first_name"]
		# Login is simply comparing the password and username in the db
		query = "SELECT * FROM users WHERE first_name = :first_name"
		data = {
			'first_name': username
		}
		result = mysql.query_db(query, data) # result is holding onto a list [] or [{}]
		 # Checking to see if there is a user by that username in the db.
		if result and bcrypt.check_password_hash(result[0]["password"], request.form["password"]):
			session["user_id"] = result[0]["id"]
			session["user_name"] = result[0]["first_name"]
			return redirect(url_for('dashboard'))
		else:
			flash("Invalid Username or Password!!!", "error")
			return redirect(url_for("login"))
	return render_template("login.html")

# checking if the user is loggedin
def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'user_id' in session:
			return f(*args, **kwargs)
		else:
			flash("You need to loggin first!", "danger")
			return redirect(url_for("login"))
	return wrap


@app.route("/dashboard/wall")
@is_logged_in
def dashboard():
	# Retrieve all existing messages from db
	query = "SELECT CONCAT(users.first_name, ' ', users.last_name) AS Full_name, messages.message AS message, messages.id AS msg_id, messages.created_at AS time_stamp  FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.id DESC"
	messages = mysql.query_db(query)

	# Retrieve all existing comments from db
	query2 = "SELECT comments.comment AS user_comment, comments.id, comments.created_at AS time_stamp, comments.message_id, CONCAT(users.first_name, ' ', users.last_name) AS full_name FROM users JOIN comments ON users.id = comments.user_id ORDER BY comments.id DESC"
	comments = mysql.query_db(query2)
	return render_template("dashboard.html", messages=messages, comments=comments)


# Route for posting messages
@app.route("/dashboard/messages", methods=["POST"])
def messages():
	# Validate the form
	msg = request.form["user_post"]
	if len(msg) < 1:
		flash("You cannot post an empty message", "error")
		return redirect(url_for("dashboard"))
	# Insert the Posted message into db
	query = "INSERT INTO messages(message, created_at, updated_at, user_id) VALUES(:message, NOW(), NOW(), :user_id)"
	data = {
		"message": request.form["user_post"],
		"user_id": session["user_id"]
	}
	mysql.query_db(query, data)
	return redirect(url_for("dashboard"))


# Route that handle posting comments
@app.route("/dashboard/comments", methods=["POST"])
def comments():
	# Validate form
	comment = request.form["comment"]
	if len(comment) < 1:
		flash("Comment cannot be empty!", "error")
	# Insert comment into db
	query = "INSERT INTO comments(comment, created_at, updated_at, message_id, user_id) VALUES(:comment, NOW(), NOW(), :message_id, :user_id)"
	data = {
		"comment": request.form["comment"],
		"message_id": request.form["msg_id"],
		"user_id": session["user_id"]
	}
	mysql.query_db(query, data)
	return redirect(url_for("dashboard"))

@app.route("/logout")
@is_logged_in
def logout():
	# I could also use session.pop('user_id')
	# session.pop("user_name")
	# You can also do: del 'user_id' from session
	session.clear()
	return redirect(url_for("login"))



app.run(debug=True)