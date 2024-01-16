from flask import  Flask,jsonify
from flask_swagger import swagger
from ADMIN_API_BP_LE.admin import admin_page
from USERS_API_BP_NS.users import users_bp
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(admin_page)
app.register_blueprint(users_bp)

@app.route('/')
def hello():
    return 'Hello World!'
@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

if __name__ == '__main__':
    app.run(debug=True)