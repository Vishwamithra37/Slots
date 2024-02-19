from flask import Flask, Blueprint, request, jsonify
import flask
from bson import json_util 
from functools import wraps
from SLOTS_BP_DIVYA import dbops as local_dbops
def resource_subresource_verification(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
         json_data=flask.request.get_json()
         admin_id = json_data["admin_id"]
         sub_resource_id=json_data["sub_resource_id"]
         slot_id=json_data["slot_id"]
         if local_dbops.verify_resource_id(admin_id) and local_dbops.verify_slotunique_id(slot_id) and local_dbops.verify_subresource_id(sub_resource_id):
    
         
                 return route_function(*args, **kwargs)

         return jsonify({"status": "error", "message": "Invalid admin id or slot id or subresource id"}), 403
         
    return decorated_function