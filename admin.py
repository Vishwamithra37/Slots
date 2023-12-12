from flask import Blueprint, jsonify
from pymongo import MongoClient

admin_bp = Blueprint('admin', __name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['movie_ticket_booking']


@admin_bp.route('/admin/register', methods=['POST'])
def admin_register():
    pass


@admin_bp.route('/admin_login', methods=['POST'])
def admin_login():
    pass

@admin_bp.route('/admin_logout', methods=['POST'])
def admin_logout():
    pass