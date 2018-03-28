from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import Form 
from wtforms import StringField
from wtforms.validators import InputRequired
import requests

app = Flask(__name__)
app.config.from_object('config.Config');

class DateForm(Form):
	date = StringField('date', validators=[InputRequired()])

	
data = {'year' : '2018', 'month' : 'march'}

@app.route('/data', methods = ['GET'])
def returnAll():
	r = requests.get('https://github.com/timeline.json')
	
	return r.text

@app.route('/data/<string:input>', methods = ['GET'])
def returnOne(input):
	if input in data:
		return data[input]
	return 'invalid input'

@app.route('/add', methods = ['GET','POST'])
def add():
	if request.methods == 'POST':
		form = DateForm(request.form)
		date = str(request.form.get('date'))
		if date.isdigit() and int(date) > 0 and int(date) < 31:
			data['date'] = date
			return str(data)
	return render_template('date.html', form = form)
	
if __name__ == '__main__':
	app.debug=True
	app.run('127.0.0.1', port = 5005)