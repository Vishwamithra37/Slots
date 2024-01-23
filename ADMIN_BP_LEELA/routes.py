import datetime
from flask import Blueprint
from flask import Flask, request, jsonify
from.config import collection  as dac
from.dbops import resource


admin_page = Blueprint('admin', __name__)

@admin_page.route('/admin/resource', methods=['POST'])
def create_resource():
    resource_data = request.get_json()
    resource_name = resource_data.get('name')
    resource_description = resource_data.get('description')
    slot_duration = resource_data.get('slot_duration')
    total_slots = resource_data.get('total_slots')
    start_date = resource_data.get('start_date')
    end_date = resource_data.get('end_date')
    slot_open_time = resource_data.get('slot_open_time')
    slot_close_time = resource_data.get('slot_close_time')
    max_bookings_per_slot = resource_data.get('max_bookings_per_slot')
    resource_obj = resource(name=resource_name,description=resource_description,slot_duration=slot_duration,total_slots=total_slots,start_date=start_date,end_date=end_date,slot_open_time=slot_open_time,slot_close_time=slot_close_time,max_bookings_per_slot=max_bookings_per_slot)
    try:
        resource_obj.validate()
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    dac.insert_one(resource_data)
    return jsonify({"message": "Resource created successfully"}), 201
    






