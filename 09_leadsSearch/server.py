from flask import Flask, render_template, redirect, request, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'lead_gen_business')
@app.route('/')
def index():
	select_query = "SELECT * FROM leads LIMIT 10"
	leads = mysql.query_db(select_query)
	return render_template('index.html', leads = leads)

@app.route('/search/name', methods=["POST"])
def search_name():
	name = request.form['name']
	print name.find(' ')
	if name.find(' ') >= 1:
		slicer = name.find(' ')
		name_1 = name[:slicer]
		name_2 = name[slicer+1:]
		select_query = "SELECT * FROM leads WHERE first_name LIKE :name_1 OR first_name LIKE :name_2 OR last_name LIKE :name_1 OR last_name LIKE :name_2"
		data = { 'name_1': '%'+name_1+'%', 'name_2': '%'+name_2+'%' }
		result = mysql.query_db(select_query, data)
		print 'this is slicing'
	else:
		select_query = "SELECT * FROM leads WHERE first_name LIKE :name OR last_name LIKE :name"
		data = { 'name': '%'+name+'%' }
		result = mysql.query_db(select_query, data)
		print 'this is not slicing'
	return jsonify(result)

@app.route('/search/date', methods=['POST'])
def serach_date():
	date_from = request.form['from']
	date_to = request.form['to']
	if len(date_to) < 1: # if To: is empty
		select_query = "SELECT * FROM leads WHERE registered_datetime > :date_from ORDER BY registered_datetime ASC"
		data = { 'date_from': date_from }
		result = mysql.query_db(select_query, data)
	elif len(date_from) < 1: # if From: is empty
		select_query = "SELECT * FROM leads WHERE registered_datetime < :date_to ORDER BY registered_datetime ASC"
		data = { 'date_to': date_to }
		result = mysql.query_db(select_query, data)
	else:
		select_query = "SELECT * FROM leads WHERE registered_datetime > :date_from AND registered_datetime < :date_to ORDER BY registered_datetime ASC"
		data = { 'date_from': date_from, 'date_to': date_to }
		result = mysql.query_db(select_query, data)
	return jsonify(result)

app.run(debug=True)
