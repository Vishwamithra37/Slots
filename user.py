from flask import Blueprint, render_template
import login_required
import hashlib
import phonenumbers

class User:
    def __init__(self, username, phone_number, password):
        self.username = username
        self.phone_number = phone_number
        self.password = hashlib.sha256(password.encode()).hexdigest()

users = []

def is_valid_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False

def register_user():
    print("User Registration:")
    username = input("Enter your username: ")
    phone_number = input("Enter your phone number: ")

    if not is_valid_phone_number(phone_number):
        print("Invalid phone number. Please enter a valid phone number.")
        return

    # Check if the username or phone number already exists
    existing_user = next((user for user in users if user.username == username or user.phone_number == phone_number), None)

    if existing_user:
        print("Username or phone number already exists. Choose a different one.")
    else:
        password = input("Enter your password: ")
        new_user = User(username, phone_number, password)
        users.append(new_user)
        print("Registration successful.")

def main():
    while True:
        print("\n1. Register\n2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            register_user()
        elif choice == '2':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()



user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def user_dashboard():
    return render_template('user_dashboard.html')
