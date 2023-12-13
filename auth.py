from flask import Blueprint, request, redirect, url_for
import flask
from pymongo import MongoClient
from blueprint import User
#from flask_login import login_user, logout_user

auth_bp = Blueprint('auth', __name__)


def login_required(func):
    if login == False:
        print("kindly login")
        return
    return func(login,logout)

allowed_email_domains=["gmail.com","yahoo.com","outlook.com","galam.in"] 
@auth_bp.route('/login', methods="post")    
def login():
    # Implement login logic here
    if flask.request.method == 'POST':
        dict1_data = flask.request.get_json()
        email= dict1_data["email"]
        user_emailchecker=User_Finder.emailfinder(email)
        email_domain = email.split('@')[1]                  #email splitting
        if email_domain  not in allowed_email_domains:      # domain checking 
           return"invalid email"
        if user_emailchecker:
          return "already registered using this email"
        else:
           if User_Finder.register_new_user(dict1_data['first_name'],dict1_data['last_name'],dict1_data['password'],dict1_data['email'],dict1_data['contact']):
              return "Registered successfully"
        return "Try again"
        
        
    
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
