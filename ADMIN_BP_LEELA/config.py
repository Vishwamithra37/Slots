from pymongo import MongoClient
import global_config
client = MongoClient("localhost", 27017)
db = client["Slotzz"]
resource_collection = db[global_config.COLLECTION_RESOURCE_DETAILS]
sub_resource_collection = db[global_config.COLLECTION_SUBRESOURCE_DETAILS]
slot_collection = db[global_config.COLLECTION_SLOT_DETAILS]
admin_collection = db[global_config.COLLECTION_ADMIN_DETAILS]
booking_resource_details = db[global_config.BOOKING_RESOURCE_COLLECTION]