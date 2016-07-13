from flask import Flask, render_template, request, redirect, jsonify, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql".
# note that you pass the data base name to the function
mysql = MySQLConnector(app, 'notesdb')
@app.route('/')
def index():
	select_query = "SELECT * FROM notes"
	notes = mysql.query_db(select_query)
	return render_template('index.html', notes = notes)
@app.route('/notes/add', methods=['POST'])
def notes_add():
	insert_query = "INSERT INTO notes (title, created_at, updated_at) VALUES (:title, NOW(), NOW())"
	data = { 'title': request.form['title'] }
	mysql.query_db(insert_query, data)
	select_query = "SELECT * FROM notes"
	notes = mysql.query_db(select_query)
	return jsonify(notes)
@app.route('/notes/update/<id>', methods=['POST'])
def notes_update(id):
	try:
		update_query = "UPDATE notes SET title = :title, description = :description, updated_at = NOW() WHERE id = :id"
		data = {
					'title': request.form['title'],
					'description': request.form['description'],
					'id': id,
				}
		mysql.query_db(update_query, data)
	except:
		update_query = "UPDATE notes SET description = :description, updated_at = NOW() WHERE id = :id"
		data = {
					'description': request.form['description'],
					'id': id,
				}
		mysql.query_db(update_query, data)
	select_query = "SELECT * FROM notes"
	notes = mysql.query_db(select_query)
	return jsonify(notes)
@app.route('/notes/delete/<id>', methods=['POST'])
def notes_delete(id):
	delete_query = "DELETE FROM notes WHERE id = :id"
	data = { 'id': id }
	mysql.query_db(delete_query, data)
	select_query = "SELECT * FROM notes"
	notes = mysql.query_db(select_query)
	return jsonify(notes)
app.run(debug=True)
