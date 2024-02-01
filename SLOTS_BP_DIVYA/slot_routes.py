from flask import Flask, Blueprint, request, jsonify
import flask
from bson import json_util 
import pymongo
from pymongo import mongo_client
from ADMIN_BP_LEELA.routes import admin_page
from decorators import adminloginrequired

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Assuming MongoDB is running locally
db = client["Slotzz"]
bookings_collection= db["Bookings"]
collection = db["create_slot"]

# Define Flask Blueprint for slot operations
slots_bp = Blueprint('slots', __name__)
@adminloginrequired
@slots_bp.route('/user/book_slot', methods=['POST'])
def book_slot():
    booking_data = request.get_json()
    user_email =booking_data["user_email"]
    slot_name = booking_data["_name"]
    date = booking_data["date"]
    time = booking_data["time"]
    seats = booking_data["seats"]

    # Check if the user exists
    user = collection.find_one({"email":user_email})
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Check if the slot is available and has seats
    slot = collection.find_one({
        'name': slot_name,
        'start_date': {"$lte": date},
        'end_date': {"$gte": date},
        'slot_open_time': {"$lte": time},
        'slot_close_time': {"$gte": time}
    })

    if not slot:
        return jsonify({'error': 'Slot not found or unavailable at the specified time'}), 400
    if slot['total_slots'] < seats:
        return jsonify({'error': 'Not enough seats available for booking'}), 400

    # Create and save the booking
    booking = {
        "user_id": user["_id"],
        "slot_id": slot["_id"],
        "date": date,
        "time": time,
        "seats": seats
    }
    collection.insert_one(booking)
    return jsonify({"message": "Slot booked succesfully"})

@slots_bp.route('//booking_history', methods=['GET'])
def booking_history(user_email):
    user = collection.find_one({"email": user_email})
    if not user:
        return jsonify({"error": "User not found"}), 404

    bookings = collection.find({"user_id": user["_id"]})
    booking_history = []
    for booking in bookings:
        slot = collection.find_one({'_id': booking["slot_id"]})
        booking["slot_name"] = slot["name"]
        booking["_id"] = str(booking["_id"])
        booking_history.append(booking)

    return jsonify(booking_history)
