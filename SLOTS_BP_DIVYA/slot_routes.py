from flask import Flask, Blueprint, request, jsonify
from bson import json_util 
import pymongo
from pymongo import mongo_client
#from ADMIN_BP_LEELA.admin import admin_page

app = Flask(__name__)

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Assuming MongoDB is running locally
db = client["Slotzz"]
dac = db["slots"]

# Define Flask Blueprint for slot operations
slots_bp = Blueprint('slots', __name__)
@slots_bp.route('/get_available_slots', methods=['GET'])
def get_available_slots():
    try:
        # Business logic for retrieving available slot
        available_slots= dac.find({'number_of_slots': True})
        available_slots_data =list(available_slots)
        if available_slots_data: #if available slots are found 
            return json_util.dumps(available_slots_data)  # Serialize the response for get_available_slots using json_util
        else:
            return jsonify({'message': 'No available slots found'}), 202  # Return 404 status if no available slots are found
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving available slots'}), 500  # Return 500 status for any errors

if __name__ == "__main__":
    app.run(debug=True)
 