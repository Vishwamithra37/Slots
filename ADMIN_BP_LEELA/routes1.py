from flask import Blueprint, Flask, request, jsonify
from .config import collection as dac
from .config import admin_collection
from .config import booking_resource_details
from .dbops import Resource  
from .dbops import Resource1
from .dbops import Resource2
from decorators import admin_login_required,login_required
from . import fun


admin_page = Blueprint('admin', __name__)

@admin_page.route('/v1/create_resource', methods=['POST'])
@login_required
def create_resource(user_details):
    resource_data = request.get_json()
    resource_obj = Resource1(name=resource_data["name"], 
                            description=resource_data["description"],
                           admin_id=resource_data["admin_id"])
    
    try:
        if not  resource_obj.validate_name(resource_data["name"]):
        
            print(type(resource_obj))
            raise ValueError("Invalid resource data:check the name and admin id")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    

    existing = dac.find_one({'admin_id': resource_data['admin_id']})
    if existing:
       return jsonify({'error': 'ID already exists'}), 400
    
    
    result=dac.insert_one(resource_data)
    if result.acknowledged:
       r1= fun.create_admin_details(user_details["Email"],resource_data["admin_id"])
       admin_collection.insert_one(r1)   
    return jsonify({"message": "Resource created successfully"}), 201


@admin_page.route('/v1/booking/resource', methods=['POST'])
@login_required
def booking_resource(user_details):
    resource_data = request.get_json()
    resource_obj = Resource2(slot_duration=resource_data["slot_duration"],
                            total_slots=resource_data["total_slots"],
                            start_date=resource_data["start_date"],
                            end_date=resource_data["end_date"], 
                            slot_open_time=resource_data["slot_open_time"], 
                            slot_close_time=resource_data["slot_close_time"],
                            max_bookings_per_slot=resource_data["max_bookings_per_slot"], 
                            admin_id=resource_data["admin_id"])
    
    existing = dac.find_one({'admin_id': resource_data['admin_id']})
    if existing:
        
     existing = booking_resource_details.insert_one(resource_data)
    return jsonify ({"message": "Booking details saved successfully"}), 201

@admin_page.route('/v1/admin/resources', methods=['GET'])
def get_all_resources():
    resources = [doc for doc in dac.find()]
    for doc in resources:
        doc["_id"] = str(doc["_id"])
    return jsonify(resources)

@admin_page.route("/v1/admin/delete_slot", methods=["POST"])
@login_required
@admin_login_required
def delete_slot(user_details):
    Email = request.get_json("Email")
    admin_id = request.get_json("admin_id")
    delete = {"Email": Email}
    
    if not Email or not admin_id:
        return {"error": "Email and admin ID are required"}, 400
    
   
    r1 = admin_collection.find_one_and_delete(delete)
    if r1:
        return "Messages deleted successfully"
    else:
        return "Failed to delete messages"
        
     

@admin_page.route('/v1/admin/update_resource',methods=['Put'])
@login_required
@admin_login_required
def update_by_admin_id(admin_id):
    resource_data = request.get_json()
    Email = request.get_json()
    if not Email or not admin_id:
        return {"error": "Email and admin ID are required"}, 400
    try:
        if not resource_data:
            raise ValueError("Invalid resource data:check the email and admin id")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    r1 = admin_collection.find_one({"Email": Email})
    if r1:
        r2=dac.find_one({"admin_id":admin_id})
        if r2:
            r3=dac.find_one_and_update({"admin_id":admin_id},{"$set":resource_data})
            if r3:
                return jsonify({"message": "Resource updated successfully"}), 201
            else:
                return jsonify({"error": "Failed to update resource"}), 400
   

