from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to python server"


# from controller.signup import signup
from controller import *