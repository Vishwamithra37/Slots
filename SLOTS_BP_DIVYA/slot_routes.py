from flask import Flask, Blueprint, request, jsonify
import flask
from bson import json_util 
import pymongo
from pymongo import mongo_client
from ADMIN_BP_LEELA.routes import admin_page
#from ADMIN_BP_LEELA.admin import admin_page


# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Assuming MongoDB is running locally
db = client["Slotzz"]
bookings_collection= db["Bookings"]
collection = db["create_slot"]

# Define Flask Blueprint for slot operations
slots_bp = Blueprint('slots', __name__)

@slots_bp.route('/available_slots', methods=['GET'])
def available_slots():
    # Logic to retrieve and return available slots from the database
    available_slots = bookings_collection.find({"available": True})  # Example query to find available slots
    slot_list = []
    for slot in available_slots:
        slot_info = {
            'slot_id': slot['_id'],
            'time': slot['time'],  # Replace with actual time field from the database
            'resource_id': slot['resource_id']  # Replace with the actual resource ID field from the database
            # Add other relevant slot information as needed
        }
        slot_list.append(slot_info)
    return jsonify({'available_slots': slot_list})

@slots_bp.route('/book_slot', methods=['POST'])
def book_slot():
    data = request.json
    email = data.get('email')
    resource_id = data.get('resource_id')
    slot_id = data.get('slot_id')


    if not email or not resource_id or not slot_id:
        return jsonify({'error': 'Incomplete information'})

    if has_required_access(email):
        if is_valid_slot(resource_id, slot_id):
            booking_data = {
                'email': email,
                'resource_id': resource_id,
                'slot_id': slot_id
            }
            booked_slots = bookings_collection.insert_one(booking_data)
            if booked_slots.inserted_id:
                return jsonify({'message': 'Slot booked successfully'})
            else:
                return jsonify({'error': 'Failed to book slot'})
        else:
            return jsonify({'error': 'Invalid slot or slot unavailable'})
    else:
        return jsonify({'error': 'Unauthorized access'})

def has_required_access(email):
    # Logic to validate user's access, e.g., user authentication
    # Replace with actual access control logic
    return True  # Placeholder for access control, update as per requirements

def is_valid_slot(resource_id, slot_id):
    # Business logic to validate slot availability and constraints
    # Replace with actual validation logic, e.g., checking against existing bookings
    return True  # Placeholder for validation, update as per requirements



# Route for fetching the number of available slots
@slots_bp.route('/get_available_slots', methods=['GET'])
def get_available_slots():
    available_slots = get_available_slots_from_database()
    return jsonify({"available_slots": available_slots}), 200

# Function to get the number of available slots from the database
def get_available_slots_from_database():
    total_created_slots = bookings_collection.count_documents({})  # Count the total number of created slots
    total_booked_slots = bookings_collection.count_documents({"status": "booked"})  # Count the total number of booked slots
    available_slots = total_created_slots - total_booked_slots  # Calculate the number of available slots
    return available_slots
# Route for fetching the details of available slots
