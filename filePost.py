import os
from flask import Flask, flash, request, redirect, url_for, render_template, abort
from flask import send_from_directory
from werkzeug.utils import secure_filename
import requests
import socket               
import sys


UPLOAD_FOLDER = '/mnt/c/Folder'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config.from_object('config.Config');
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

##
port_list = [5005,5010];
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#request from multiple servers
#work as a tcp clientside.
@app.route('/echo')
def echo():
             
    host = '127.0.0.1'
    result = ''.encode()
    for port in port_list:
	    s = socket.socket() # Create a socket object
	    s.connect((host, port))
	    result += s.recv(1024) #receive the first 1024 bytes from socket and concatenation bytes together
	    message = 'get'.encode()
	    s.send(message)
	    s.close()
    return result

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
#get file from multiple servers.http(not completed)

@app.route('/get2', methods = ['GET'])
def returnAll():
	r = ''
	address = ['http://208.80.154.224',	'https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Sending_and_Receiving_Binary_Data']
	for ip in address:
		r += requests.get(ip).text	#str += r.text
	return r

'''
if __name__ == '__main__':
    app.debug=True
    app.run('127.0.0.1', port = 5000)