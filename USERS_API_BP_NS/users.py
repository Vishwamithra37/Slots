from flask import Flask,current_app,Blueprint, jsonify, request,session,flash,url_for
from flask_mail import Mail, Message
from pymongo import MongoClient, UpdateOne
import os
from user_functions import User_Finder
from bson import ObjectId
import random
import string
import bcrypt
import jwt
from bson.binary import Binary
import base64

#app = Flask(__name__)
#secret_key = os.urandom(24)
#app.secret_key = secret_key

users_bp = Blueprint('users', __name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['Slotzz']
dac =db["Account_holders"]
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/slotzzz'
#mongo = PyMongo(app)

"""app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'navyasri.uv@gmail.com'
app.config['MAIL_PASSWORD'] = 'navya@1234'

mail = Mail(app)"""

@users_bp.route('/user_register', methods=['POST'])
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
  Fullname = users_data['Fullname']
  #lastname = users_data['lastname']
  Email = users_data['Email']
  Contact_no = users_data['Contact_no']
  Password = users_data['Password']
  Confirm_password = users_data['Confirm_password']
  accepted_domains = ["gmail.com", "yahoo.com", "outlook.com", "slotzz.in"]
  if not any(Email.endswith(domain) for domain in accepted_domains):
            return "Invalid email domain. Allowed domains: gmail.com, yahoo.com, outlook.com, slotzz.in"


  if len(Password) < 8 or not (any(c.isdigit() for c in Password) and any(c.isalpha() for c in Password) and any(not c.isalnum() for c in Password)):
            return "Password should be at least 8 characters and contain at least one digit, one letter, and one special character"

  existing_user = dac.find_one({"Email": users_data['Email']})
  if users_data['Password'] != users_data['Confirm_password']:
    return "Password and confirm password didn't match. Please re-enter your password."
  if existing_user:
        return 'User with this emailid already exists. Please use a different email or proceed to the user login page.'
  hashed_password = bcrypt.hashpw(users_data['Password'].encode('utf-8'), bcrypt.gensalt())
  users_data['Password'] = hashed_password
  hashed_password1 = bcrypt.hashpw(users_data['Confirm_password'].encode('utf-8'), bcrypt.gensalt())
  users_data['Confirm_password'] = hashed_password1
  users_data['Permissions'] = ['view_slots', 'book_slot',"cancel_booking", "view_history", "profile_update", "profile_view"]
  dac.insert_one(users_data)
  return 'Congratulations! User registered successfully. You can now proceed to the login. '



@users_bp.route('/user_login', methods=['POST'])
def user_login():
    
    
    users_data = request.get_json()
    email = users_data['email']
    password = users_data['password']
    user = dac.find_one({"email": email})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        token = jwt.encode({'email': email, 'permissions': user['permissions']}, current_app.secret_key, algorithm='HS256')
        session['token'] = token
        welcome_message = "Welcome to the Slotzz!\n" + user["firstname"] + "\n! You are now logged in.\n\nWhat would you like to do today?\n1. View Available Slots\n2. Book a Slot\n3. Cancel a Booking\n4. My Bookings\n5. Logout\n\nPlease enter the number corresponding to your desired action."
        return welcome_message
    else:
        return 'Invalid credentials'
             


@users_bp.route('/user_logout', methods=['POST'])
def user_logout():
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
    session.pop('users', None)
    return 'You have been logged out.'

@users_bp.route('/password-reset-request', methods=['POST'])
def password_reset_request():
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
    email = request.json['email']
    user =  User_Finder.emailfinder(email)
    if user:
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        
        dac.update_one({'email': email}, {'$set': {'reset_token': token}})
        return jsonify({'message': 'Password reset token has been sent to your email'})
    else:
        return jsonify({'error': 'User not found'})

@users_bp.route('/password-reset', methods=['POST'])
def password_reset():
    email = request.json['email']
    token = request.json['token']
    new_password = request.json['new_password']
    user = dac.find_one({'email': email, 'reset_token': token})
    if user:
        hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        # Update the user's password in the database with the hashed password
        dac.update_one({'email': email}, {'$set': {'password': hashed_new_password}, '$unset': {'reset_token': 1}})
        return jsonify({'message': 'Password has been reset successfully'})
    else:
        return jsonify({'error': 'Invalid token'})
      


@users_bp.route('/user_profile_edit', methods=['PUT'])
def edit_user_profile():
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
    user_data = request.get_json()   
    email = user_data["email"]   
    new_email = user_data["new_email"]   
    new_contact = user_data["new_contact"] 
    result = dac.update_one({'email': email}, {'$set': {'email': new_email, 'contact': new_contact}}) 

    if result.modified_count > 0: 
        user = User_Finder.emailfinder(new_email) 
        if user:
            user["email"] = new_email
            user['contact'] = new_contact
            return "User profile updated successfully"
        else:
            return "User profile updated in the database, but user data retrieval failed"
    else:
        return "User not found"   
    
@users_bp.route('/user_profile_view/<email>', methods=['GET'])
def view_profile(email):
    
    user_data = request.get_json() 
    email = user_data["email"]
    user_profile = dac.find_one({"email": email})

    if user_profile:
        user_profile['_id'] = str(user_profile['_id'])
        user_profile['password'] = user_profile['password'].decode('utf-8')

        return jsonify(user_profile)
    else:
        current_app.logger.error("User profile not found for email: email")
        return jsonify({"message": "User profile not found"}), 404   



def send_welcome_email(firstname, email):
    users_data = request.get_json()
    email = users_data['email']
    user_details=User_Finder.emailfinder(email)
    if user_details:
    
     msg = Message('Welcome to Slotzz', sender='your_email@example.com', recipients=[email])
    #msg.body = "Thank you," +  user_details["firstname"]," +  "for registering with Slotzz! Enjoy your slot booking experience."
    mail.send(msg)

if __name__ == '__main__':
  app.run(debug=True)
