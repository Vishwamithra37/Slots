import flask
from .config import collection
import global_config
from flask_mail import Mail
from bson import ObjectId
from bson import json_util
import os
import datetime
from flask import request, session, flash

class DAC(object):
    def __init__(self, client=None):
        self.client = client or global_config.MONGOCLIENT
    
    def find_one(self, email):
        return self.client['Account_holders'].find_one({'Email': email})
    
    def update_one(self, email, update):
        return self.client['Account_holders'].update_one({'Email': email}, update)
    
    def insert_one(self, data):
        return self.client['Account_holders'].insert_one(data)
    
    def delete_one(self, email):
        return self.client['Account_holders'].delete_one({'Email': email})

class Mail:
    def __init__(self, app):
        self.app = app
    
    def send(self, email, subject, message):
        self.app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        self.app.config['MAIL_PORT'] = 587
        self.app.config['MAIL_USE_TLS'] = True
        self.app.config['MAIL_USER'] = 'navyasri.uv@gmail.com'
        self.app.config['MAIL_PASSWORD'] = 'navya@1234'
        self.app.config['MAIL_OPTS'] = {'Client': 'gmail'}
       # mail = Mail(app)
        #mail.send(email, subject, message)
