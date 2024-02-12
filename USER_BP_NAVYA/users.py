from flask import Flask,current_app,Blueprint, jsonify,json, request,session,flash
from flask_mail import Mail, Message
import flask
from pymongo import MongoClient, UpdateOne
import os
import datetime
from .user_functions import User_Finder
from bson import ObjectId
from bson import json_util
import random
import string
import bcrypt
import jwt
from bson.binary import Binary
import base64
import global_config
from decorators import login_required



users_bp = Blueprint('users', __name__)
client = MongoClient(global_config.MONGOCLIENT)
db = client[global_config.DB]
dac =db["Account_holders"]


"""app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'navyasri.uv@gmail.com'
app.config['MAIL_PASSWORD'] = 'navya@1234'

mail = Mail(app)"""

@users_bp.route('/v1/user_register', methods=['POST'])
def user_register():
  """user_register
      ---
      tags: 
        - "Users"
      
      description: "Endpoint to register a new user with validation checks"
      parameters:
        - in: "body"
          name: "user"
          description: "User registration details"
          required: true
          schema:
            type: "object"
            properties:
              Fullname:
                type: "string"
              Email:
                type: "string"
              Contact_no:
                type: "string"
              Password:
                type: "string"
              Confirm_password:
                type: "string"
      responses:
        200:
          description: "User registered successfully"
          
        400:
          description: "Bad request"
          
        409:
          description: "User already exists"
          
        422:
          description: "Validation error"
           """
  

  users_data = request.get_json()
  print(users_data)
  Fullname = users_data['Fullname']
  Email = users_data['Email']
  Contact_no = users_data['Contact_no']
  Password = users_data['Password']
  Confirm_password = users_data['Confirm_password']
  accepted_domains = global_config.ACCEPTED_DOMAINS
  if not any(Email.endswith(domain) for domain in accepted_domains):
            return jsonify({'message' : "Invalid email domain. Allowed domains: gmail.com, yahoo.com, outlook.com, slotzz.in"}), 400


  if len(Password) < 8 or not (any(c.isdigit() for c in Password) and any(c.isalpha() for c in Password) and any(not c.isalnum() for c in Password)):
            return  jsonify ({'message' : "Password should be at least 8 characters and contain at least one digit, one letter, and one special character"}), 400
  if not Contact_no.isdigit() or len(Contact_no) != 10:
    return jsonify ({'message' : "Invalid contact number format. Please enter a 10-digit number."}), 400


  existing_user = dac.find_one({"Email": users_data['Email']})
  if users_data['Password'] != users_data['Confirm_password']:
    return  jsonify ({'message' : "Password and confirm password didn't match. Please re-enter your password."}), 400
  if existing_user:
        return jsonify({'message':'User with this emailid already exists. Please use a different email or proceed to the user login page.'}),400
  hashed_password = bcrypt.hashpw(users_data['Password'].encode('utf-8'), bcrypt.gensalt())
  users_data['Password'] = hashed_password
  hashed_password1 = bcrypt.hashpw(users_data['Confirm_password'].encode('utf-8'), bcrypt.gensalt())
  users_data['Confirm_password'] = hashed_password1
  users_data['Permissions'] = global_config.PERMISSIONS
  dac.insert_one(users_data)
  return  jsonify({'message' : 'Congratulations! User registered successfully. You can now proceed to the login.'}), 200



@users_bp.route('/v1/user_login', methods=['POST'])
def user_login():
    
    users_data = request.get_json()
    print(users_data)
    Email = users_data['Email']
    Password = users_data['Password']

    user = dac.find_one({"Email": Email})
    if user and bcrypt.checkpw(Password.encode('utf-8'), user['Password']):
     token = jwt.encode({'Email': Email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'], algorithm='HS256')
     user['token'] = token 
     dac.update_one({"Email": Email}, {"$set": {"token": token}})
     flask.session.update({"token":token})
     #session['token'] = token

     welcome_message = f"Welcome to the Slotzz, {user['Fullname']}! You are now logged in. What would you like to do today?\n1. View Available Slots\n2. Book a Slot\n3. Cancel a Booking\n4. My Bookings\n5. Logout\n\nPlease enter the corresponding number for your desired action."
     return jsonify({'message': welcome_message, 'token': token})
    else:
     return jsonify({'message': 'Invalid username or password'}), 401

  
@users_bp.route('/v1/user_logout', methods=['POST'])
@login_required
def user_logout(user_details):
    """swagger: '2.0'
info:
  title: User Logout API
  version: 1.0.0
paths:
  /user_logout:
    post:
      summary: Log out the user
      responses:
        200:
          description: User has been logged out successfully
          schema:
            type: string
            example: You have been logged out."""
    Email=user_details["Email"]
    print("Session Data Before Logout:", session)
    session.pop('token', None) 
    print("Session Data After Logout:", session)
    result = dac.update_one({"Email": Email},{"$unset": {"token": ""}})
    if result.modified_count:
     logout_message = "You have been successfully logged out. Thank you for using Slotzz!"
     return jsonify({'message': logout_message})
    return {"status":"Logout failed,Try again"},400

@users_bp.route('/v1/password-reset-request', methods=['POST'])
@login_required
def password_reset_request(user_details):
    """swagger: '2.0'
info:
  title: Password Reset API
  version: 1.0.0
paths:
  /password-reset-request:
    post:
      summary: Request password reset
      consumes:
        - application/json
      parameters:
        - in: body
          name: body
          required: true
          schema:
            type: object
            properties:
              email:
                type: string
                example: user@example.com
      responses:
        200:
          description: Password reset token has been sent to the user's email
          schema:
            type: object
            properties:
              message:
                type: string
                example: Password reset token has been sent to your email
        404:
          description: User not found
          schema:
            type: object
            properties:
              error:
                type: string
                example: User not found

  /password-reset:
    post:
      summary: Reset user's password
      consumes:
        - application/json
      parameters:
        - in: body
          name: body
          required: true
          schema:
            type: object
            properties:
              email:
                type: string
                example: user@example.com
              token:
                type: string
                example: reset_token
              new_password:
                type: string
                example: new_password
      responses:
        200:
          description: Password has been reset successfully
          schema:
            type: object
            properties:
              message:
                type: string
                example: Password has been reset successfully
        404:
          description: Invalid token
          schema:
            type: object
            properties:
              error:
                type: string
                example: Invalid token"""
  
    Email=user_details['Email']

    token = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
    dac.update_one({'Email': Email}, {'$set': {'reset_token': token}})
    return jsonify({'message': 'Password reset token has been sent to your email'})
    

@users_bp.route('/v1/password-reset', methods=['POST'])
@login_required
def password_reset(user_details):
    Email = user_details['Email']
    token = request.json['token']
    new_password = request.json['new_password']
    user = dac.find_one({'Email': Email, 'reset_token': token})
    if user:
        hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        # Update the user's password in the database with the hashed password
        dac.update_one({'Email': Email}, {'$set': {'Password': hashed_new_password}, '$unset': {'reset_token': 1}})
        return jsonify({'message': 'Password has been reset successfully'})
    return jsonify({'error': 'Invalid token'})
      


@users_bp.route('/v1/user_profile_edit', methods=['POST'])
@login_required
def edit_user_profile(user_details):
    """
    Update user profile
    ---
    tags:
      - users
    description: Endpoint for updating a user's profile information
    parameters:
      - in: body
        name: user_data
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              description: The user's email
            new_email:
              type: string
              description: The new email to be updated
            new_contact:
              type: string
              description: The new contact information
    responses:
      200:
        description: User profile updated successfully
      404:
        description: User not found
    """
    print(flask.session) 
    Email = user_details["Email"]  
    print("Email:", Email)
    user_data = request.get_json()
    new_contact = user_data["new_contact"] 
    print("new_contact:", new_contact)
    if not new_contact.isdigit() or len(new_contact) != 10:
      return jsonify ({'message' : "Invalid contact number format. Please enter a 10-digit number."}), 400
    result = dac.update_one({'Email': Email}, {'$set': {'Contact_no': new_contact}}) 
    if result.modified_count > 0:
        return {"message":"User profile updated successfully"}
    return {"message":"User not found"},400
    
@users_bp.route('/v1/user_profile_view', methods=['POST'])
@login_required
def view_profile(user_details):
        user_details['_id'] = str(user_details['_id'])
        del user_details["Password"]
        del user_details["Confirm_password"]
        del user_details["token"]
        return {"message":user_details}
    
      


def send_welcome_email(firstname, email):
    users_data = request.get_json()
    email = users_data['email']
    user_details=User_Finder.emailfinder(email)
    if user_details:
    
     msg = Message('Welcome to Slotzz', sender='your_email@example.com', recipients=[email])
    #msg.body = "Thank you," +  user_details["firstname"]," +  "for registering with Slotzz! Enjoy your slot booking experience."
    mail.send(msg)


