from flask import Flask, render_template, request, redirect, jsonify, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql".
# note that you pass the data base name to the function
mysql = MySQLConnector(app, 'tasksdb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/show')
def show():
	select_query = "SELECT * FROM tasks"
	tasks = mysql.query_db(select_query)
	return render_template('show.html', tasks = tasks)

@app.route('/add', methods=['POST'])
def add():
	insert_query = "INSERT INTO tasks (name, created_at, updated_at) VALUES (:name, NOW(), NOW())"
	data = { 'name': request.form['new_task'] }
	mysql.query_db(insert_query, data)
	return render_template('index.html')

@app.route('/edit/<id>', methods=['POST'])
def edit(id):
	update_query = "UPDATE tasks SET name = :name, updated_at = NOW() WHERE id = :id"
	data = { 'name': request.form['name'], 'id': id }
	mysql.query_db(update_query, data)
	return render_template('index.html')

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
	delete_query = "DELETE FROM tasks WHERE id = :id"
	data = { 'id': id }
	mysql.query_db(delete_query, data)
	return render_template('index.html')

app.run(debug=True)
