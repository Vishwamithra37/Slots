from flask import Flask, Blueprint, request, jsonify
import flask
from bson import json_util 
import pymongo
from pymongo import mongo_client
from ADMIN_BP_LEELA.routes import admin_page
from decorators import login_required
from USER_BP_NAVYA.users import users_bp
import global_config
from bson.json_util import dumps
import jwt

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Assuming MongoDB is running locally
db = client["Slotzz"]
bookings_collection= db["Bookings"]
ACCOUNT_HOLDERS_COLLECTION= db[global_config.ACCOUNT_HOLDERS_COLLECTION]
RESOURCE_DETAILS_COLLECTION= db[global_config.COLLECTION_RESOURCE_DETAILS]


# Define Flask Blueprint for slot operations
slots_bp = Blueprint('slots', __name__)
@login_required
@slots_bp.route('/book_slot', methods=['POST'])
def book_slot():
    booking_data = request.get_json()
    title_name= booking_data["title_name"],
    resource_name = booking_data["resource_name"]
    date = booking_data["date"]
    time = booking_data["time"]
    seats = booking_data["seats"]

    #to find the slot from the resource collection
    slot = RESOURCE_DETAILS_COLLECTION.find_one({
        'name': resource_name
    
    })
    print(slot)
    if not slot:
        return jsonify({'error': 'Slot not found or unavailable at the specified time'}), 400
    
    # Create and save the booking

    booking_data = {
        "title_name": title_name,
        "resource_name": resource_name,
        "date": date,
        "time": time,
        "seats": seats
    }
    if booking_data["date"] < slot["start_date"] or booking_data["date"] > slot["end_date"]:
     return "Date is outside the slot's valid range"

    if booking_data["time"] < slot["slot_open_time"] or  booking_data["time"] >slot["slot_close_time"]:
     return "Time is outside the slot's valid range"

    if booking_data["seats"] <= slot["total_slots"]:
    # Create and save the booking here
       bookings_collection.insert_one(booking_data)
       return "Slot booked successfully"

    else:
     return "Not enough seats available for booking"
    
@slots_bp.route('/user/booking_history', methods=['GET'])
def booking_history():
    booking_history=request.get_json()
    Email = booking_history['Email'] 
    user = ACCOUNT_HOLDERS_COLLECTION.find_one({"Email":Email})
    if not user:
        return jsonify({"error": "User not found"}), 404

    booking_history = bookings_collection.find({"user_id": user["_id"]})
    booking_history = list(booking_history)
    #to get the booking history
    json_booking_history = dumps(booking_history)
    return json_booking_history
