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
from bson import ObjectId
from SLOTS_BP_DIVYA import dbops
from SLOTS_BP_DIVYA import mydecorators

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Assuming MongoDB is running locally
db = client["Slotzz"]
bookings_collection= db["Bookings"]
ACCOUNT_HOLDERS_COLLECTION= db[global_config.ACCOUNT_HOLDERS_COLLECTION]
RESOURCE_DETAILS_COLLECTION= db[global_config.COLLECTION_RESOURCE_DETAILS]


# Define Flask Blueprint for slot operations
slots_bp = Blueprint('slots',__name__)

@slots_bp.route('/v1/book_slot', methods=['POST'])
@login_required
@mydecorators.resource_subresource_verification
def book_slot(data):
    """This route is used to book a slot by the required information provided by the user

    Args:
        data (dict):  Contains all the necessary information about the user who wants to book a slot

    Returns:
        type: string--contains the message showing that weather the booking operation was succesful or not.  
        If successful then it returns the Slot booked successfully else Not enough seats available for booking.
    """
    booking_data = request.get_json()
    ResourceID = booking_data["admin_id"]
    SubResourceID = booking_data["SubResourceID"]
    SlotUniqueID = booking_data["slot_id"]
    #title_name= booking_data["title_name"],
    #resource_name = booking_data["resource_name"]
    date = booking_data["date"]
    time = booking_data["time"]
    seats = booking_data["seats"]
    
    # Create and save the booking

    booking_data = {
        #"title_name": title_name,
        #"resource_name": resource_name,
        "date": date,
        "time": time,
        #"seats": seats
    }
    if booking_data["date"] < slot["start_date"] or booking_data["date"] > slot["end_date"]:
     return "Date is outside the slot's valid range"

    if booking_data["time"] < slot["slot_open_time"] or  booking_data["time"] >slot["slot_close_time"]:
     return "Time is outside the slot's valid range"

    if booking_data["seats"] <= slot["total_slots"]:
    # Create and save the booking here
       bookings_collection.insert_one(booking_data)
       return "Slot booked successfully"
    return "Not enough seats available for booking"
    
@slots_bp.route('/v1/view_booking_history', methods=['GET'])
@login_required
def booking_history(user_details):
    """This route provides the user with booking history through the Email of the user_details

    Args:
        user_details (dict):  A dictionary containing details about a logged in user

    Returns:
        type: string -- returns a message stating user booking history which  includes all their bookings
    """
    Email = user_details['Email']
    booking_history = bookings_collection.find({"user_id": user_details["_id"]})
    booking_history = list(booking_history)
    #to get the booking history
    json_booking_history = dumps(booking_history)
    return {"user_booking_history":json_booking_history},200

@slots_bp.route('/v1/cancel_booking/<string:_id>', methods=['DELETE'])
@login_required
def cancel_booking(user_details,_id):
    """This route allows you to cancel the booking through booking id

    Args:
        user_details (dict): these are the user details which are retrieved @login_required
        _id (string): it is the object_Id when booking is created

    Returns:
        type:  string -- It returns a message stating whether cancellation was successful or not
    """
    # Check if the booking exists

    booking = bookings_collection.find_one({"_id": ObjectId(_id)})
    if booking:
        # Delete the booking from the database
        bookings_collection.delete_one({"_id": ObjectId(_id)})
        return "Booking canceled successfully"
    return "Booking not found for the provided ID"