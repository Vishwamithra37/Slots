import pymongo
from global_config import ACCOUNT_HOLDERS_COLLECTION, COLLECTION_RESOURCE_DETAILS
from bson import ObjectId
import global_config

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Assuming MongoDB is running locally
db = client["Slotzz"]
bookings_collection = db["Bookings"]
RESOURCE_DETAILS_COLLECTION = db[COLLECTION_RESOURCE_DETAILS]
COLLECTION_SUBRESOURCE_DETAILS=db[global_config.COLLECTION_SUBRESOURCE_DETAILS]
COLLECTION_SLOT_DETAILS=db[global_config.COLLECTION_SLOT_DETAILS]

def verify_resource_id(admin_id):
    if RESOURCE_DETAILS_COLLECTION.find_one({"AdminID": admin_id}):
        return True
    return False

def verify_slotunique_id(unique_id):
    if COLLECTION_SLOT_DETAILS.find_one({"UniqueID":  unique_id}):
        return True
    return False
def verify_subresource_id(unique_id):
    if COLLECTION_SUBRESOURCE_DETAILS.find_one({"UniqueID":  unique_id}):
        return True
    return False

                                        
    


def get_booking_history(user_id):
    booking_history = bookings_collection.find({"user_id": user_id})
    return list(booking_history)

def cancel_booking_by_id(booking_id):
    booking = bookings_collection.find_one({"_id": ObjectId(booking_id)})
    if booking:
        bookings_collection.delete_one({"_id": ObjectId(booking_id)})
        return True
    return False