from flask import Blueprint, jsonify, request
from pymongo import MongoClient

users_bp = Blueprint('users', __name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['movie_ticket_booking']


@users_bp.route('/user/register', methods=['POST'])
def user_register():
 pass

@users_bp.route('/user_login', methods=['POST'])
def user_login():
    pass

@users_bp.route('/user_logout', methods=['POST'])
def user_logout():
    pass