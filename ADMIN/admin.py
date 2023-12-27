from flask import Flask,Blueprint,jsonify
from pymongo import MongoClient
from admin_functions import Admin_Finder

app = Flask(__name__)

admin_bp = Blueprint('admin', __name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['Slotzz']
dac =db["Account_holders"]


@admin_bp.route('/admin/register', methods=['POST'])
def admin_register():
    admin_data = Flask.request.get_json()
    if not admin_data:
        return 'Data not provided'
    firstname = admin_data['firstname']
    lastname = admin_data['lastname']
    email = admin_data['email']
    contact = admin_data['contact']
    password=admin_data["password"]
    accepted_domains = ["gmail.com", "yahoo.com", "outlook.com", "slots.in"]
    if not any(email.endswith(domain) for domain in accepted_domains):
            return "Invalid email domain. Allowed domains: gmail.com, yahoo.com, outlook.com, slots.in"

    
    if len(firstname) > 25:
        return 'First name should be below 25 characters'
    
    if len(password) < 8 or not (any(c.isdigit() for c in password) and any(c.isalpha() for c in password) and any(not c.isalnum() for c in password)):
            return "Password should be at least 8 characters and contain at least one digit, one letter, and one special character"

    existing_admin = Admin_Finder.emailfinder(email)
    if existing_admin:
        return 'Admin with this emailid already exists. Please use a different email or proceed to the admin login page.'
    else:
         if Admin_Finder.get_admin_data(admin_data["firstname"],admin_data["lastname"],admin_data["email"],admin_data["contact"]):
             return 'Congratulations! Admin registered successfully. You can now proceed to the admin login. '
    return "Try Again"


@admin_bp.route('/admin_login', methods=['POST'])
def admin_login():
    pass

@admin_bp.route('/admin_logout', methods=['POST'])
def admin_logout():
    pass


if __name__ == '__main__':
    app.run(debug=True)
