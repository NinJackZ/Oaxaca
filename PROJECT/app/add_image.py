from flask import Flask, Blueprint, render_template, request, redirect, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from app.extensions import db
from app.models import Orders,Menu
import os

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file from the request
    file = request.files['file']

    # Create a folder to store the file if it doesn't exist
    if not os.path.exists('uploads'):
        os.mkdir('uploads')

    # Save the file to the uploads folder
    file.save(os.path.join('uploads', file.filename))

    # Return a success message
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()
