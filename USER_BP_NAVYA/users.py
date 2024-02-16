from flask import Flask,current_app,Blueprint, jsonify,json, request,session,flash
from flask_mail import Mail, Message
import flask
from pymongo import MongoClient, UpdateOne
import os
from datetime import datetime,timedelta
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
from .dbops import find_user_by_email,update_user_fields
from USER_BP_NAVYA.input_validations import validate_fullname


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
  """This route registers a new user in the system.
  
  Keyword arguments:
  argument -- "Fullname" (string) : The user's fullname.
              "Email" (string): The user's email address.
              "Contact_no" (string): The user's contact number.
              "Password" (string): The user's password ( hashed with bcrypt).
              "Confirm_password" (string): The user's confirm password (hashed with bcrypt).

  Return:  A JSON response with a success message if the user is registered successfully, or an error message otherwise.
  """
  users_data = request.get_json()
  Fullname = users_data['Fullname']
  Email = users_data['Email']
  Contact_no = users_data['Contact_no']
  Password = users_data['Password']
  Confirm_password = users_data['Confirm_password']
  accepted_domains = global_config.ACCEPTED_DOMAINS
  fullname_validation_result = validate_fullname(Fullname)
  if fullname_validation_result:
    return jsonify(fullname_validation_result), 400
  if not any(Email.endswith(domain) for domain in accepted_domains):
            return jsonify({'message' : "Invalid email domain. Allowed domains: gmail.com, yahoo.com, outlook.com, slotzz.in"}), 400
  if len(Password) < 8 or not (any(c.isdigit() for c in Password) and any(c.isalpha() for c in Password) and any(not c.isalnum() for c in Password)):
            return  jsonify ({'message' : "Password should be at least 8 characters and contain at least one digit, one letter, and one special character"}), 400
  if not Contact_no.isdigit() or len(Contact_no) != 10:
    return jsonify ({'message' : "Invalid contact number format. Please enter a 10-digit number."}), 400
  if users_data['Password'] != users_data['Confirm_password']:
    return  jsonify ({'message' : "Password and confirm password didn't match. Please re-enter your password."}), 400
  existing_user = find_user_by_email(dac, users_data['Email'])
  if existing_user:
        return jsonify({'message':'User with this emailid already exists. Please use a different email or proceed to the user login page.'}),400
  hashed_password = bcrypt.hashpw(users_data['Password'].encode('utf-8'), bcrypt.gensalt())
  hashed_password1 = bcrypt.hashpw(users_data['Confirm_password'].encode('utf-8'), bcrypt.gensalt())
  users_data['Password'], users_data['Confirm_password'] = hashed_password, hashed_password1
  users_data['Permissions'] = global_config.PERMISSIONS
  dac.insert_one(users_data)
  return  jsonify({'message' : 'Congratulations! User registered successfully. You can now proceed to the login.'}), 200



@users_bp.route('/v1/user_login', methods=['POST'])
def user_login():
    """This route Logs in a user using their email and password, and returns a JWT token for authentication.

    Keyword arguments:
    argument --  (Request) The request object containing the user's data in JSON format.
                "Email" (string): The user's email address.
                "Password" (string): The user's password ( hashed with bcrypt).

    
    Return: token: (String) The JWT token for authentication.
            message: (String) A welcome message for the user after logging in, otherwise an error message 
    """
    
    users_data = request.get_json()
    print(users_data)
    Email = users_data['Email']
    Password = users_data['Password']

    user = find_user_by_email(dac, users_data['Email'])
    if user and bcrypt.checkpw(Password.encode('utf-8'), user['Password']):
     token = jwt.encode({'Email': Email, 'exp': datetime.utcnow() + timedelta(minutes=30)}, current_app.config['SECRET_KEY'], algorithm='HS256')
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
    """This route Logs out a user and removes their JWT token from the session.
    
    Keyword arguments:
    argument -- "Email" (string) the email address of user to logout
    Return: message (string) A success message after logout or returns an error message upon unsuccessful attempt
    """
    
    
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
    """This route generates a password reset token 
    
    Keyword arguments:
    argument -- "Email" (string)The email address of user
    Return: message (string) - A success message after generating the password reset token.
    """
    
  
    Email=user_details['Email']
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    dac.update_one({'Email': Email}, {'$set': {'reset_token': token}})
    return jsonify({'message': 'Password reset token has been sent to your email'})
    

@users_bp.route('/v1/password-reset', methods=['POST'])
@login_required
def password_reset(user_details):
    """This routes resets a user's password using a password reset token.

    
    Keyword arguments:
    argument -- "Email" {string} - The email address of the user to reset the password for.
                "token" {string} - The password reset token generated in the password reset request route.
                "new_password" {string} - The new password to set for the user.

    Return: message {string} - A success message after resetting the password.
    """
    
    Email = user_details['Email']
    token = request.json['token']
    new_password = request.json['new_password']
    user = dac.find_one({'Email': Email, 'reset_token': token})
    if user:  
         hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
         dac.update_one({'Email': Email}, {'$set': {'Password': hashed_new_password}, '$unset': {'reset_token': 1}})
         return {'message': 'Password has been reset successfully'}
    return {'error': 'Invalid token'}
      


@users_bp.route('/v1/user_profile_edit', methods=['POST'])
@login_required
def edit_user_profile(user_details):
    """This route edits a user's profile information(contact number)

    
    Keyword arguments:
    argument --  "Email" {string} - The email address of the user to edit the profile for.
                 "new_contact" (string) - The new contact number which user uses in future.
                

    Return: message {string} - A success message after updating the user's profile.
    """
    
    print(flask.session) 
    Email = user_details["Email"]  
    print("Email:", Email)
    user_data = request.get_json()
    new_contact = user_data["new_contact"] 
    print("new_contact:", new_contact)
    if not new_contact.isdigit() or len(new_contact) != 10:
      return jsonify ({'message' : "Invalid contact number format. Please enter a 10-digit number."}), 400
    update_fields = {
    'Contact_no': new_contact}
    result_count = update_user_fields(dac, Email, update_fields)
    if result_count > 0:
        return {"message":"User profile updated successfully"}
    return {"message":"User not found"},400
    
@users_bp.route('/v1/user_profile_view', methods=['POST'])
@login_required
def view_profile(user_details):
        """This route displays a user's profile information, excluding their password and token.

        
        Keyword arguments:
        argument -- user_ {json} - The user's profile information.

        Return: message {string} - The user's profile information.
        """
        
        user_details['_id'] = str(user_details['_id'])
        del user_details["Password"]
        del user_details["Confirm_password"]
        del user_details["token"]
        return {"message":user_details}
    
      


def send_welcome_email(user_details,firstname, email):
    users_data = request.get_json()
    email = user_details['email']
    if user_details:
    
     msg = Message('Welcome to Slotzz', sender='your_email@example.com', recipients=[email])
    #msg.body = "Thank you," +  user_details["firstname"]," +  "for registering with Slotzz! Enjoy your slot booking experience."
    Mail.send(msg)


