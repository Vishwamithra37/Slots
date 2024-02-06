from pymongo import MongoClient
import global_config
client = MongoClient("localhost", 27017)
db = client["Slotzz"]
collection = db[global_config.COLLECTION_RESOURCE_DETAILS]
admin_collection = db[global_config.COLLECTION_ADMIN_DETAILS]
booking_resource_details = db[global_config.BOOKING_RESOURCE_COLLECTION]