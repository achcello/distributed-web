import os
from flask import Flask, request, redirect, url_for, render_template
from flask import send_from_directory
from werkzeug.utils import secure_filename
import requests


UPLOAD_FOLDER = '/mnt/c/plusOrWhateverThePathIs'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ip_list = [];

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('get_file',
                                    filename=filename))
    return render_template('fileSubmit.html')
	

#get file and try to split them;
@app.route('/get/<filename>')
def get_file(filename):
	path = app.config['UPLOAD_FOLDER'] + filename;
	
	file = open(path,'r')
	#str = split_page(file.read(),2)[1] not subscriptable?
	#return file.readlines()[0] but this works.
	return file.read()
'''
#get file from multiple servers.

@app.route('/get2', methods = ['GET'])
def returnAll():
	str = ''
	for ip in ip_list:
		r = requests.get(ip)
		str += r.text
	return z
'''

if __name__ == '__main__':
	app.debug=True
	app.run('127.0.0.1', port = 5000)