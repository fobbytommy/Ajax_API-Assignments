from flask import Flask, render_template, request, redirect, jsonify, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql".
# note that you pass the data base name to the function
mysql = MySQLConnector(app, 'postsdb')
@app.route('/')
def index():
	select_query = "SELECT description FROM posts ORDER BY created_at DESC"
	posts = mysql.query_db(select_query)
	return render_template('index.html', posts = posts)
@app.route('/posts/create', methods=['POST'])
def create():
	insert_query = "INSERT INTO posts (description, created_at, updated_at) VALUES (:description, NOW(), NOW())"
	data = { "description": request.form['description'] }
	mysql.query_db(insert_query, data)
	select_query = "SELECT description FROM posts ORDER BY created_at DESC"
	posts = mysql.query_db(select_query)
	return jsonify(posts)
app.run(debug=True)
