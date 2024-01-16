from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["Slotzz"]
collection = db["Account_holders"]
