from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, "mydb")

app.secret_key = "hfHEugptiip[oht[p"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


# home page
@app.route("/")
def index():
	return render_template("index.html")

# Success Page
@app.route("/success", methods=["POST"])
def success():
	if not EMAIL_REGEX.match(request.form["email"]):
		flash("Invalid Email Address!", "error")
		return redirect("/")
	if EMAIL_REGEX.match(request.form["email"]):
		flash("The email address you entered '{}' is a valid email, Thank you!".format(request.form["email"]), "success")
		# Insert email into the db
		query = "INSERT INTO emails (email_address, created_at, updated_at) VALUES(:email, NOW(), NOW())"
		data = {
			"email": request.form["email"]
		}
		mysql.query_db(query, data)
		# Retrive all emails from db
		query = "SELECT * FROM emails ORDER BY emails.id DESC"
		emails = mysql.query_db(query)
	return render_template("success.html", all_emails = emails)

# Delete a particular email from db
@app.route("/delete_email/<email_id>")
def remove_email(email_id):
	query = "DELETE FROM emails WHERE id = :email"
	data = {
		"email": email_id
	}
	mysql.query_db(query, data)
	return redirect(url_for("success"))


app.run(debug=True)