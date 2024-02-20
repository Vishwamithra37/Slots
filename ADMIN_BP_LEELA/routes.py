from flask import Blueprint, Flask, request, jsonify
from .config import resource_collection,sub_resource_collection,slot_collection,admin_collection
from .config import admin_collection
from .dbops import Resource1,Resource2,Resource3
from decorators import admin_login_required,login_required
from . import fun
from global_config import COLLECTION_ADMIN_DETAILS,COLLECTION_RESOURCE_DETAILS as crd,COLLECTION_SLOT_DETAILS,COLLECTION_SUBRESOURCE_DETAILS

admin_page = Blueprint('admin', __name__)

@admin_page.route('/admin/create_resource', methods=['POST'])
@login_required
def create_resource(user_details):
    resource_data1 = request.get_json()
    resource_obj1 = Resource1(resource_name=resource_data1["resource_name"],
                            description=resource_data1["description"],
                            resource_unique_id=resource_data1["resource_unique_id"],
                            resource_tags = resource_data1["resource_tags"],
                            creator_email= user_details ["Email"])

    if resource_obj1.validate_resource_name(resource_data1["resource_name"]) == False:
        return jsonify({"Message":"Resource name should be atleast 3 characters"}),400
    if resource_obj1.validate_description(resource_data1["description"]) == False:
        return jsonify({"Message": "Description should contain at least 5 words and not more than 100 words"}),400
    if resource_obj1.validate_unique_admin_id(resource_data1["resource_unique_id"]) == False:
         return jsonify({"Error": "Admin already has a resource with this Admin ID and check the length of admin id ."}),400
        
    if resource_obj1.validate_resource_tags(resource_data1["resource_tags"])==False:
        return jsonify({"Message":"Invalid tags"}),400
       
    
    
    else:
        result=resource_collection.insert_one(resource_obj1.__dict__)
        
    if result.acknowledged:
       r1= fun.create_admin_details(user_details["Email"],resource_data1["resource_unique_id"])
       admin_collection.insert_one(r1)   
    return jsonify({"message": "Resource created successfully"}), 201


       

@admin_page.route("/sub_resource", methods=['POST'])
@login_required
@admin_login_required
def create_sub_resource(user_details):
    resource_data2 = request.get_json()
    resource_obj2 = Resource2(sub_resource_name=resource_data2["sub_resource_name"],
                              sub_description=resource_data2["sub_description"],
                              sub_resource_id=resource_data2["sub_resource_id"],
                              resource_unique_id=resource_data2["resource_unique_id"] )

    if resource_obj2.validate_sub_resource_name(resource_data2["sub_resource_name"]) == False:
        return jsonify({"Message": "Sub-Resource name should be atleast 3 characters"}), 400
    if resource_obj2.validate_sub_description(resource_data2["sub_description"]) == False:
        return jsonify({"Message": "Description should contain at least 5 words and not more than 100 words"}), 400
    if resource_obj2.validate_sub_resource_id(resource_data2["sub_resource_id"]) == False:
        return jsonify({"Error": "Sub-Resource ID already exists"}), 400

    result = sub_resource_collection.insert_one(resource_obj2.__dict__)
    return jsonify({"Message": "Successfully created Sub-Resource"}), 201

@admin_page.route("/create_slot", methods=["post"]) 
def create_slot():
    slot_data = request.get_json()   
    slot_obj = Resource3(Slot_name=slot_data["Slot_name"],
                        Slot_description=slot_data["Slot_description"],
                        Status = slot_data["Status"],
                        StartTime = slot_data["StartTime"],
                        EndTime = slot_data["EndTime"],
                        MaxAdvanceDays = slot_data["MaxAdvanceDays"],
                        MaxBookings = slot_data["MaxBookings"],
                        Daysofweek = slot_data["Daysofweek"],
                        resource_unique_id = slot_data["resource_unique_id"],
                        sub_resource_id= slot_data["sub_resource_id"],
                        slot_unique_id= slot_data["slot_unique_id"]
                        )
    
    if slot_obj.validate_slot_name(slot_data["Slot_name"]) == False:
        return jsonify({"Message": "Please enter a valid Slot Name."}), 
    if slot_obj.validate_slot_description(slot_data["Slot_description"]) == False:
        return jsonify({"Message": "Please enter a valid Slot Description."}),
    if slot_obj.validate_status(slot_data["Status"]) == False:
        return jsonify({"Message": "Please enter a valid Status."}),
    if slot_obj.validate_start_time(slot_data["StartTime"]) == False:
        return jsonify({"Message": "Please enter a valid Start Time."}),
    if slot_obj.validate_end_time(slot_data["EndTime"]) == False:
        return jsonify({"Message": "Please enter a valid End Time."}),
    if slot_obj.validate_max_advance_days(slot_data["MaxAdvanceDays"]) == False:
        return jsonify({"Message": "Please enter a valid Max Advance Days."}),
    if slot_obj.validate_max_bookings(slot_data["MaxBookings"]) == False:
        return jsonify({"Message": "Please enter a valid Max Bookings."}),
    if slot_obj.validate_days_of_week(slot_data["Daysofweek"]) == False:
        return jsonify({"Message": "Please enter a valid Days of Week."}),
    if slot_obj.validate_resource_id(slot_data["resource_unique_id"]) == False:
        return jsonify({"Message": "Please enter a valid Resource Unique ID."}),
    if slot_obj.validate_sub_resource_unique_id(slot_data["sub_resource_id"]) == False:
        return jsonify({"Message": "Please enter a valid Sub Resource Unique ID."}),
    if slot_obj.validate_unique_slot_id(slot_data["slot_unique_id"]) == False:
        return jsonify({"Message": "Please enter a valid Slot Unique ID."}),


    result = slot_collection.insert_one(slot_obj.__dict__)
    return jsonify({"Message": "Successfully created Slot"}), 201



@admin_page.route('/admin/resources', methods=['GET'])
def get_all_resources():
    resources = [doc for doc in resource_collection.find()]
    for doc in resources:
        doc["_id"] = str(doc["_id"])
    return jsonify(resources)

@admin_page.route("/admin/delete_slot", methods=["POST"])
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
        
     

@admin_page.route('/admin/update_resource',methods=['Put'])
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
        r2=resource_collection.find_one({"admin_id":admin_id})
        if r2:
            r3=resource_collection.find_one_and_update({"admin_id":admin_id},{"$set":resource_data})
            if r3:
                return jsonify({"message": "Resource updated successfully"}), 201
            else:
                return jsonify({"error": "Failed to update resource"}), 400
   

