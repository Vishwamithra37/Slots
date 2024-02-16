import flask
from .config import collection
import global_config
from bson import ObjectId
from bson import json_util
import os
import datetime
from flask import request, session, flash

def find_user_by_email(collection, email):
    """This function finds users email from Account_holders collection"""
    user_details = collection.find_one({"Email": email})
    return user_details

def update_user_fields(collection, email, updated_fields):
    """This function updates user details(new_contact,new_password) in Account_holders collelction """
    update_query = {'$set': updated_fields}
    result = collection.update_one({'Email': email}, update_query)
    return result.modified_count if result else 0 






