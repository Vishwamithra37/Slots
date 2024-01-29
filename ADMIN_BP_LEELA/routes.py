from flask import Blueprint, Flask, request, jsonify
from .config import collection as dac
from .dbops import Resource  


admin_page = Blueprint('admin', __name__)

@admin_page.route('/admin/resource', methods=['POST'])
def create_resource():
    resource_data = request.get_json()
    resource_obj = Resource(name=resource_data["name"], description=resource_data["description"],
                            slot_duration=resource_data["slot_duration"], total_slots=resource_data["total_slots"], start_date=resource_data["start_date"],
                            end_date=resource_data["end_date"], slot_open_time=resource_data["slot_open_time"], slot_close_time=resource_data["slot_close_time"],
                            max_bookings_per_slot=resource_data["max_bookings_per_slot"], admin_id=resource_data["admin_id"])
    

    try:
        if not resource_obj.validate():
            raise ValueError("Invalid resource data:check the name and admin id")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    

    existing = dac.find_one({'admin_id': resource_data['admin_id']})
    if existing:
       return jsonify({'error': 'ID already exists'}), 400
    existing = dac.find_one({'name': resource_data['name']})
    if existing:
        return jsonify({'error': 'Name already exists'}), 400
    dac.insert_one(resource_data)
    return jsonify({"message": "Resource created successfully"}), 201
@admin_page.route('/admin/resources', methods=['GET'])
def get_all_resources():
    resources = [doc for doc in dac.find()]
    for doc in resources:
        doc["_id"] = str(doc["_id"])
    return jsonify(resources)
@admin_page.route('/admin/resource/<int:admin_id>',methods=['GET'])
def get_by_admin_id(admin_id):
    resources = [doc for doc in dac.find({"admin_id":admin_id})]
    for doc in resources:
        doc["_id"] = str(doc["_id"])
    return jsonify(resources)
@admin_page.route('/admin/delete_resource/<int:admin_id>',methods=['post'])
def delete_by_admin_id(admin_id):
    if request.args.get('delete')=='true':
        dac.delete_one({"admin_id":admin_id})
        return jsonify({"message": "Resource deleted successfully"}), 201
    else:
        return jsonify({"message": "Resource not deleted"}), 201

@admin_page.route('/admin/update_resource/<int:admin_id>',methods=['Put'])
def update_by_admin_id(admin_id):
    resource_data = request.get_json()
    resource_obj = Resource(name=resource_data["name"], description=resource_data["description"],
                            slot_duration=resource_data["slot_duration"], total_slots=resource_data["total_slots"], start_date=resource_data["start_date"],
                            end_date=resource_data["end_date"], slot_open_time=resource_data["slot_open_time"], slot_close_time=resource_data["slot_close_time"],
                            max_bookings_per_slot=resource_data["max_bookings_per_slot"], admin_id=resource_data["admin_id"])
    category=resource_data["category"], status=resource_data["status"],
    try:
        if not resource_obj.validate():
            raise ValueError("Invalid resource data:check the name and admin id")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    result = dac.update_one({"admin_id": admin_id}, {"$set": resource_data})
    if result.matched_count == 0:
        return jsonify({"error": "Resource not found"}), 404
    return jsonify({"message": "Resource updated successfully"}), 201







