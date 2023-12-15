from flask import Flask,url_for
from users import users_bp
from admin import admin_bp

app = Flask(__name__)

app.register_blueprint(users_bp, url_prefix='/users_rel_routes')
app.register_blueprint(admin_bp, url_prefix='/admin_rel_routes')

if __name__ == '__main__':
    app.run(debug=True)