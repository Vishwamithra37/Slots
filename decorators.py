from flask import session,url_for,redirect
import flask
from functools import wraps
import global_config
from pymongo import MongoClient

client = MongoClient(global_config.MONGOCLIENT)
db = client[global_config.DB]
dac =db["Account_holders"]




def login_required(route_function):
    @wraps(route_function)
    def wrapper_function(*args, **kwargs):
        print(flask.session)
        if "token" not in flask.session:
            return {"status": "error", "message": "Login required"}, 401
        token = flask.session["token"]
        #user = get_user_details_by_token(token)

        #if user:
            #flask.g.user = user
        return route_function(*args, **kwargs)

    return wrapper_function



def get_user_details_by_token(token):
    user = dac.find_one({"token": token})  
    return user
