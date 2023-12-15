from flask import Flask,Blueprint, jsonify, request,session,flash,url_for
from flask_mail import Mail, Message
from flask_pymongo import PyMongo
from pymongo import MongoClient
import os
from user_functions import User_Finder

app = Flask(__name__)
secret_key = os.urandom(24)
app.secret_key = secret_key


users_bp = Blueprint('users', __name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['Slotzz']
dac =db["Account_holders"]
app.config['MONGO_URI'] = 'mongodb://localhost:27017/slotzzz'
mongo = PyMongo(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'navyasri.uv@gmail.com'
app.config['MAIL_PASSWORD'] = 'navya@1234'

mail = Mail(app)

@users_bp.route('/user_register', methods=['POST'])
def user_register():
    users_data = request.get_json()
    firstname = users_data['firstname']
    lastname = users_data['lastname']
    email = users_data['email']
    contact = users_data['contact']
    password = users_data['password']
    accepted_domains = ["gmail.com", "yahoo.com", "outlook.com", "slotzz.in"]
    if not any(email.endswith(domain) for domain in accepted_domains):
            return "Invalid email domain. Allowed domains: gmail.com, yahoo.com, outlook.com, slotzz.in"


    if len(password) < 8 or not (any(c.isdigit() for c in password) and any(c.isalpha() for c in password) and any(not c.isalnum() for c in password)):
            return "Password should be at least 8 characters and contain at least one digit, one letter, and one special character"

    existing_user = User_Finder.emailfinder(email)
    if existing_user:
        return 'User with this emailid already exists. Please use a different email or proceed to the user login page.'
    else:
         if User_Finder.get_user_data(users_data["firstname"],users_data["lastname"],users_data["email"],users_data["contact"],users_data["password"]):
             return 'Congratulations! User registered successfully. You can now proceed to the login. '
    return "Try Again"


@users_bp.route('/user_login', methods=['POST'])
def user_login():
    users_data = request.get_json()
    email = users_data['email']
    password = users_data['password']

    user_details=User_Finder.emailfinder(email)
    if user_details:
             welcome_message = f"Welcome to the Slotzz!\n""\nHi + user_data.get("fisrtname")\n" + "! You are now logged in.\n\nWhat would you like to do today?\n1. View Available Slots\n2. Book a Slot\n3. Cancel a Booking\n4. My Bookings\n5. Logout\n\nPlease enter the number corresponding to your desired action."
             return welcome_message
    return "Invalid credentials"


@users_bp.route('/user_logout', methods=['POST'])
def user_logout():
    session.pop('user', None)
    return 'You have been logged out.'

@app.route('/book_slot', methods=['POST'])
def book_slot():
    data = request.get_json()
    slot_id = data.get('slot_id')
    # Add logic to book the slot in the database
    return {'message': f'Slot {slot_id} booked successfully.'}, 200

def send_welcome_email(username, email):
    msg = Message('Welcome to Slot Booking App', sender='your_email@example.com', recipients=[email])
    msg.body = f'Thank you, {username}, for registering with Slot Booking App! Enjoy your slot booking experience.'
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
