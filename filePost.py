import os
from flask import Flask, flash, request, redirect, url_for, render_template, abort
from flask import send_from_directory
from werkzeug.utils import secure_filename
import requests


UPLOAD_FOLDER = '/mnt/c/Folder'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config.from_object('config.Config');
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ip_list = [];
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/post', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            abort(404)
			
        file = request.files['file']
        # if user does not select file, or a file not allowed
        if file.filename == ''or allowed_file(file.filename) != True:
            abort(404)
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
	
	file = open(path,'rb')
	#str = split_page(file.read(),2)[1] not subscriptable?
	#return file.readlines()[0] #but this works.
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