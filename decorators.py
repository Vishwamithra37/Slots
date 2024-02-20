from flask import session,url_for,redirect,jsonify
import flask
from functools import wraps
import global_config
from pymongo import MongoClient
from  ADMIN_BP_LEELA.config import admin_collection


client = MongoClient(global_config.MONGOCLIENT)
db = client[global_config.DB]
dac =db["Account_holders"]




def login_required(route_function):
    @wraps(route_function)
    def wrapper_function(*args, **kwargs):
        print(flask.request.headers)
        if "token" not in flask.session:
            return {"status": "error", "message": "Login required"}, 401
        token = flask.session["token"]
        user = get_user_details_by_token(token)
        Permission_name=route_function.__name__
        
        if user:
           
            if Permission_name in user.get("Permissions"):
                print("decorator is working")
                return route_function(user_details=user,*args, **kwargs)
            else:
                return jsonify({"status": "error", "message": "Insufficient permission"}), 403
        else:
            return jsonify({"status": "error", "message": "Invalid token"}), 401

    return wrapper_function
        

def get_user_details_by_token(token):
    try:
        user = dac.find_one({"token": token})  
        if user:
            return user
        else:
            return None  
    except Exception as e:
        
        return None  
    
def admin_login_required(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        
         admin_id = flask.request.get_json()["admin_id"]
         user_email=kwargs["user_details"]["Email"]
        
         Permission_name=route_function.__name__
         print("this is from admin login_required")
         print(Permission_name)
         admin_permissions=admin_collection_verification(admin_id,user_email)
         if admin_permissions:
             if Permission_name in admin_permissions:
                 print(" admin login decorator is working")
                 return route_function(*args, **kwargs)
             else:
                 return jsonify({"status": "error", "message": "Insufficient permissions"}), 403
         else:
             return jsonify({"status": "error", "message": "Invalid admin id"}), 401

             

    return decorated_function

def admin_collection_verification(admin_id,user_email):
    admin_details = admin_collection.find_one({"email": user_email,"admin_id":admin_id})
    if admin_details:
        return admin_details["Permissions"]

    return False
