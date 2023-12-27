from bson import ObjectId
from flask import Flask, Blueprint, request, jsonify
from pymongo import MongoClient 

routes_bp = Blueprint('routes',__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['Slotzz'] 
collection = db['slots'] 

@routes_bp.route('/available_slots', methods=['GET'])
def get_available_slots():
    """THis route will list all the available slots"""
    available_slots = list(collection.find({'status': 'available'}))
    for slot in available_slots:
        slot['_id'] = str(slot['_id'])
    return jsonify({'available_slots': available_slots})

@routes_bp.route('/create_slot', methods=['POST'])
def create_slot():
    slot_data = request.json
    new_slot_id = collection.insert_one(slot_data).inserted_id
    return jsonify({'message': 'Slot created successfully', 'slot_id': str(new_slot_id)})

@routes_bp.route('/delete_slot/<slot_id>', methods=['DELETE'])
def delete_slot(slot_id):

    result = collection.delete_one({'_id': ObjectId(slot_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Slot deleted successfully'})
    else:
        return jsonify({'message': 'Slot not found or could not be deleted'}, 404)


