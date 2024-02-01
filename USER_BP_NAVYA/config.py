from pymongo import MongoClient
import global_config

client = MongoClient("localhost", 27017)
db = client["Slotzz"]
collection = db[global_config.ACCOUNT_HOLDERS_COLLECTION]
