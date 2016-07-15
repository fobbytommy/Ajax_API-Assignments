from flask import Flask, render_template, request, redirect
import requests
import urllib
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/direction', methods=['POST'])
def direction():
	origin = request.form['origin']
	destination = request.form['destination']
	# package the post data from our form into a dictionary
	data = {'origin':origin, 'destination':destination}
	api_key = "AIzaSyBF7R8aPR_AOQ0OuJg5KGOvrUKM1gcN9ow"
	url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + urllib.urlencode(data) + "&key=" + api_key
	response = requests.get(url).content
	print url, urllib.urlencode(data)
	return response

app.run(debug=True)
