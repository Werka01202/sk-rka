# -*- coding: utf-8 -*-
import os
import uuid
from flask import flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from Skornik import app

app.secret_key = "Skornik@123#SuperSecretKey"
UPLOAD_FOLDER = os.path.join('Skornik','static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Widok strony g³ównej
@app.route('/')
def home():
    return render_template('index.html')

# Widoki pozosta³ych stron
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/page1')
def page1():
    return "This is Page 1."

@app.route('/page2')
def page2():
    return "This is Page 2."

@app.route('/page3')
def page3():
    return "This is Page 3."


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash("No file found in request.")
        return redirect(url_for('home'))

    file = request.files['file']
    if file.filename == '':
        flash("No file selected.")
        return redirect(url_for('home'))

    if file and allowed_file(file.filename):
        # Generowanie unikalnej nazwy pliku
        filename = f"{uuid.uuid4().hex}{os.path.splitext(file.filename)[1]}"
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            file.save(upload_path)
            flash("File successfully uploaded.")
            return render_template('upload_success.html', filename=filename)
        except Exception as e:
            print(f"Error saving file: {e}")
            flash("An error occurred while saving the file.")
            return redirect(url_for('home'))
    else:
        flash("Invalid file type. Allowed types: PNG, JPG, JPEG, GIF.")
        return redirect(url_for('home'))