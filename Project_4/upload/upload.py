import os

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from werkzeug import secure_filename
import subprocess
UPLOAD_FOLDER = '/tmp/upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def encrypt_file(encryptfile, password):    
    archive_file = encryptfile + '.zip'
    password_params = '-p' + password
    # create archive
    rc = subprocess.call(['7z', 'a', password_params, '-y', archive_file] + [encryptfile])
    
    return archive_file

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    
    if request.method =='POST':
        if request.form['username'] == '':
            error = 'Null username'
        elif request.form['password'] == '':
            error = 'Null password'
            
        else:
            password = request.form['password']
            return redirect(url_for('upload_file'))
    return render_template('login.html', error=error)
    
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # encrypt file
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fname = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            archive_file = encrypt_file(fname, '1234')
            
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

from flask import send_from_directory

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)    

if __name__ == '__main__':
    app.run(debug=True)
