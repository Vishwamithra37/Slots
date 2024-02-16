from flask import  Flask,jsonify,render_template
import flask
from flask_swagger import swagger
from ADMIN_BP_LEELA.routes1 import admin_page
#from ADMIN_BP_LEELA.routes import admin_page
from USER_BP_NAVYA.users import users_bp
from SLOTS_BP_DIVYA.slot_routes import slots_bp
import os
from decorators import login_required

app = Flask(__name__)
app.secret_key = "this is my secret key"

app.register_blueprint(admin_page)
app.register_blueprint(users_bp)
app.register_blueprint(slots_bp)




@app.route('/home')
@login_required
def home():
    return  flask.render_template('home.html')

@app.route('/about')
@login_required
def about_page():
    return  flask.render_template('About.html')

@app.route('/history')
@login_required
def history_page():
    return  flask.render_template('History.html')

@app.route('/resource')
@login_required
def resource_test():
    return  flask.render_template('Resource.html')

@app.route('/signuppage')
@login_required
def signup_test():
    return  flask.render_template('signup.html')


@app.route('/loginpage')
@login_required
def login_test():
    return  flask.render_template('login.html')


@app.route('/')
def hello():
    return 'Hello World!'
#trail 

@app.route("/spec")
@login_required
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

if __name__ == '__main__':
    app.run(debug=True)