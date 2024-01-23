import datetime
from flask import Blueprint
from flask import Flask, request, jsonify
from.config import collection  as dac
from.dbops import validation 




app = Flask(__name__)
admin_page = Blueprint('admin', __name__,static_folder="admin_static",template_folder="admin_template")

@admin_page.route('/admin/create_slot', methods=['POST'])
def create_slot():
    data = request.get_json()
    slot_name = data.get('slot_name')
    resource = data.get('resource')
    date_str = data.get('date')
    time_str = data.get('time')
    number_of_slots = data.get('number_of_slots')

    # Validation of date and time input
    if not validation.validate_date(date_str):
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD."}), 400
    if not validation.validate_time(time_str):
        return jsonify({"error": "Invalid time format. Please use HH:MM in 24-hour format."}), 400

    # Convert date and time strings to datetime object
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    time_obj = datetime.datetime.strptime(time_str, '%H:%M')

    # Combine date and time into a single datetime object
    combined_datetime = datetime.datetime.combine(
        date_obj.date(), time_obj.time())

  
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




