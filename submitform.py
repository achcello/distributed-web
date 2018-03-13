from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import Form 
from wtforms import StringField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config.from_object('config.Config');

	
class SubmittForm(Form):
	name = StringField('name', validators=[InputRequired()])
	status = StringField('s', validators=[InputRequired()])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = SubmittForm(request.form)
	name=request.form.get('name');
	status = request.form.get('status');
	if request.method == "POST":
		if name and status:
			return redirect(url_for('welcome', name = name))
		else:
			return render_template('Submit.html', form = form)
	return render_template('Submit.html', form = form)
	

@app.route("/welcome/<string:name>")
def welcome(name):
	return "Welcome " + name

if __name__ == '__main__':
	app.debug=True
	app.run('127.0.0.1', port = 5005)