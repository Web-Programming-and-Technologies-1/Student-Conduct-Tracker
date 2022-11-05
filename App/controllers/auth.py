# import flask_login
from flask_jwt import JWT
from App.models import User
from flask import Blueprint, render_template, jsonify, send_from_directory, flash, json, jsonify, redirect
from flask_jwt import jwt_required, JWT, current_identity
from flask import Flask, request, url_for, g
from flask_login import LoginManager, current_user, login_user, login_required, login_manager
from ..controllers.review import*
from App.controllers import *

#Authenicate a Staff based on the email and password provided
def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password=password):
        return user
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    user = User.query.get(payload['identity'])
    if user:
        return user
    return None

#Remember a user login details 
def login_user(user, remember):
    return flask_login.login_user(user, remember=remember)
    

#Allow user to logout of the system once logged in
def logout_user():
   return flask_login.logout_user()
    

def setup_jwt(app):
    return JWT(app, authenticate, identity)