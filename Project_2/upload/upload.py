import os
import subprocess
import zipfile

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'])

# secret key for session store later
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def encrypt_file(encryptfile, password):    
    archive_file = encryptfile + '.zip'
    password_params = '-p' + password
    # create archive
    rc = subprocess.call(['7z', 'a', password_params, '-y', archive_file] + [encryptfile])
    rc = subprocess.call(['rm', '-f'] + [encryptfile])
    return archive_file

# decrypt zip file to temporary /tmp/view folder
def decrypt_file(encryptedfile, encryptfile, password):
    z = zipfile.ZipFile(encryptedfile)
    try:
        f = z.open(encryptfile, 'r', pwd=password)
        return f
    except KeyError:
        print 'Error: Did not find %s in zip file' % encryptfile
    finally:
        z.close()

# create upload folder @ /tmp/upload
def create_folder():
    if not os.path.isdir(app.config['UPLOAD_FOLDER']):
        rc = subprocess.call(['mkdir'] + [UPLOAD_FOLDER])

@app.before_request
def before_request():
    create_folder()

@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method =='POST':
        if request.form['username'] == '':
            error = 'Null username'
        elif request.form['password'] == '':
            error = 'Null password'
        else:
            return redirect(url_for('choose_option'))
    return render_template('login.html', error=error)

@app.route('/choose_option', methods=['GET', 'POST'])
def choose_option():
    error = None
    if request.method == 'POST':
        if request.form['option'] == '':
            error = 'No option was chosen'
        elif request.form['option'] == "Upload":
            return redirect(url_for('upload_file'))
        elif request.form['option'] == "View":
            return redirect(url_for('view_file'))
                    
    return render_template('choose.html', error=error)

@app.route('/view_file', methods=['GET', 'POST'])
def view_file():
    error = None
    if request.method == 'POST':
        if request.form['password'] == '':
            error = 'Null password'
        else:
            file = request.files['file']
            password = request.form['password']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                fname = filename.split('.')
                fname1 = fname[0] + '.' + fname[1]
                filename1 = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                # unzip file to read and display on website
                content = decrypt_file(filename1, fname1, password )
                return render_template('display.html', content=content)
    return render_template('view.html', error=error)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    error = None
    if request.method == 'POST':
        file = request.files['file']
        password = request.form['password']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fname = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(fname)            
            archive_file = encrypt_file(fname, password)
            return redirect(url_for('choose_option'))
    return render_template('upload.html', error=error)

from flask import send_from_directory

@app.route('/view/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['VIEW_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
