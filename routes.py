from flask import Flask, request, jsonify
from pymongo import MongoClient, ReturnDocument

app = Flask(__name__)

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")
db = client["Slotz"]
slots_collection = db["slot_booking"]

# API endpoint to book a slot
@app.route('/book_slot', methods=['POST'])
def book_slot():
    data = request.json
    slot_id = data.get('slot_id')
    user_id = data.get('user_id')

    # Find and update the slot if available
    updated_slot = slots_collection.find_one_and_update(
        {"_id": slot_id, "available": True},
        {"$set": {"available": False, "user_id": user_id}},
        return_document=ReturnDocument.AFTER
    )

    if updated_slot:
        return jsonify({"message": "Slot booked successfully", "slot_details": updated_slot})
    else:
        return jsonify({"message": "Slot is not available or does not exist"})

if __name__ == '__main__':
    app.run(debug=True)

