from app import app
from model.auth import auth
from flask import request
from flask import send_file
import json


obj=auth()
@app.route('/getdata')
def getdata():
    return obj.getdata()

@app.route('/signup',methods=["POST"])
def signup():   
    return obj.signup(request)

@app.route('/upload',methods=["POST"])
def upload():
    return obj.upload(request)



@app.route('/getfile/<filename>')
def getfile(filename):
    return send_file(f"uploads/{filename}")

