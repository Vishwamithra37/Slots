import datetime
from flask import Blueprint
from pymongo import MongoClient
from flask import Flask, request, jsonify
import re


app = Flask(__name__)
client = MongoClient("localhost", 27017)
db = client["Slotzz"]
dac = db["Account_holders"]

admin_page = Blueprint('admin', __name__,static_folder="admin_static",template_folder="admin_template")


# Input validation function for date
def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Input validation function for time
def validate_time(time_str):
    if re.match(r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', time_str):
        return True
    else:
        return False

@admin_page.route('/admin/create_slot', methods=['POST'])
def create_slot():
    data = request.get_json()
    slot_name = data.get('slot_name')
    resource = data.get('resource')
    date_str = data.get('date')
    time_str = data.get('time')
    number_of_slots = data.get('number_of_slots')

    # Validation of date and time input
    if not validate_date(date_str):
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD."}), 400
    if not validate_time(time_str):
        return jsonify({"error": "Invalid time format. Please use HH:MM in 24-hour format."}), 400

    # Convert date and time strings to datetime object
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    time_obj = datetime.datetime.strptime(time_str, '%H:%M')

    # Combine date and time into a single datetime object
    combined_datetime = datetime.datetime.combine(date_obj.date(), time_obj.time())

    # Create the slot document with date, time, and number_of_slots
    slot_data = {
        "slot_name": slot_name,
        "resource": resource,
        "datetime": combined_datetime,
        "number_of_slots": number_of_slots,
        
    }
    result = dac.insert_one(slot_data)
    return jsonify({"message": "Slot created successfully", "slot_id": str(result.inserted_id)}), 200

if __name__ =='_main__':
    app.run(debug=True)




