from flask import Flask,url_for, jsonify
from flask_swagger import swagger
from users import users_bp
from routes import routes_bp
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/users_rel_routes/*": {"origins": "http://localhost:3000"}})






app.secret_key = os.urandom(24)


app.register_blueprint(users_bp, url_prefix='/users_rel_routes')
app.register_blueprint(routes_bp, url_prefix='/slot_rel_routes')


@app.route('/route_name', methods=['POST'])
def method():
    return "welcome"

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

@app.route('/trail_route', methods=['POST'])
def route_testing():
   return "successful"

if __name__ == '__main__':
    app.run(debug=True)