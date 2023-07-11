from flask import Blueprint, render_template, request, redirect, send_file, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from .models import client, mydb, mycol
from . import db
import base64
import gridfs
from pdf2image import convert_from_path
import os
import shutil

views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        file = request.files['myfile']
        file.save(secure_filename(file.filename))
        fileName = file.filename
        path = r'C:\Users\chirag.mishra\project_microservices\\'+fileName
        write_new_pdf(path, file.filename)
        return redirect('/download')
    return render_template("home.html", user=current_user)

@views.route('/download', methods=['POST', 'GET'])
def download():
    return render_template('download.html', user=current_user)

@views.route('/download2', methods=['GET', 'POST'])
def download_file():
    if request.method == 'GET':
        path = r'C:\Users\chirag.mishra\project_microservices\website\static\unconverted\converted.zip'
    return send_file(path, as_attachment=True)

@views.route('/delete', methods=['POST', 'GET'])
def delete():
    dir = r'C:\Users\chirag.mishra\project_microservices\website\static\converted'
    dir2 = r'C:\Users\chirag.mishra\project_microservices\website\static\unconverted'
    print("Delete method is being called")
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    for j in os.listdir(dir2):
        os.remove(os.path.join(dir2, j))
    return ""


def write_new_pdf(path, filename):
    print("Write function is getting called")
    fs = gridfs.GridFS(mydb)
    # Note, open with the "rb" flag for "read bytes"
    with open(path, "rb") as f:
        encoded_string = base64.b64encode(f.read())
    with fs.new_file(
        chunkSize=800000,
        filename=path) as fp:
        fp.write(encoded_string)
    read_pdf(filename)

def read_pdf(filename):
    print("Read function is getting called")
    fs = gridfs.GridFS(mydb)
    # Standard query to Mongo
    for grid_out in fs.find(filter=dict(filename=filename)).limit(1):
        data = grid_out
        with open(filename, "wb") as f:
            f.write(base64.b64decode(data.read()))
    converter(filename)

def converter(filename):
    print("Converter is being called")
    images = convert_from_path(filename,500,poppler_path=r'C:\Program Files\poppler-23.05.0\Library\bin')
    for i in range(len(images)):
        images[i].save(os.path.join(r'C:\Users\chirag.mishra\project_microservices\website\static\converted', 
                                 f"page-{i}.jpeg"), 'JPEG')
    zipMaker(filename)


def zipMaker(filename):
    print("Zip file is being created")
    print(filename)
    converted_file = shutil.make_archive(r'C:\Users\chirag.mishra\project_microservices\website\static\unconverted\converted', 'zip', r'C:\Users\chirag.mishra\project_microservices\website\static\converted')
    os.remove(filename)
            
            



