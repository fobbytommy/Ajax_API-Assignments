from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
	# this route will make the Ajax call for the client
	artist = request.form['artist']
	url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
	response = requests.get(url).content
	return response

app.run(debug=True)
