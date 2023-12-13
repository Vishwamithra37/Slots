from flask import Flask
import dbops
import config
from login_and_register_blueprint.routes import site as site_login

app = Flask(__name__)

# app.secret_key = config.SECRET_PASSWORD
app.register_blueprint(site_login, url_prefix="/Vishwa_APIs/")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)