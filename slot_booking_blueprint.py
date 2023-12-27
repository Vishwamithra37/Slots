from flask import Flask, Blueprint, request, jsonify
import pymongo
from bson import json_util 

app = Flask(__name__)

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Assuming MongoDB is running locally
db = client["Slotzz"]
dac = db["slots"]

# Define Flask Blueprint for slot operations
slots_bp = Blueprint('slots', __name__)

@slots_bp.route('/create_slot', methods=['POST'])
def create_slot():
    # Business logic for creating a new slot
    # Example: Extract slot details from the request and insert into the database
     if request.method == 'POST':
        # Retrieve slot details from the request JSON
        slot_data = request.json
        movie_title = slot_data['movie_title']
        slot_date = slot_data['slot_date']
        slot_time = slot_data['slot_time']
        availability = slot_data['availability']
          # Validate slot data
        if movie_title and slot_date and slot_time and availability is not None:
            # Create a new slot object
            new_slot = {
                'movie_title': movie_title,
                'slot_date': slot_date,
                'slot_time': slot_time,
                'availability': availability
            }
            # Insert the new slot into the collection
            result = dac.insert_one(new_slot)  # Assuming db is the MongoDB database and slots is the collection

            if result.inserted_id:
                 return json_util.dumps({'message': 'New slot created successfully', 'slot': new_slot})  # Using json_util to serialize the response
            else:
                return jsonify({'error': 'Failed to create slot'}), 500
        else:
            return jsonify({'error': 'Invalid slot data provided'}), 400
     else:
        return jsonify({'error': 'Method not allowed'}), 405

@slots_bp.route('/get_available_slots', methods=['GET'])
def get_available_slots():
    try:
        # Business logic for retrieving available slots
         available_slots = dac.find({'availability': True})
         available_slots_data =list(available_slots)
         if available_slots_data: #if available slots are found 
            return json_util.dumps(available_slots_data)  # Serialize the response for get_available_slots using json_util
         else:
            return jsonify({'message': 'No available slots found'}), 404  # Return 404 status if no available slots are found
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving available slots'}), 500  # Return 500 status for any errors

if __name__ == "__main__":
    app.run(debug=True)
 