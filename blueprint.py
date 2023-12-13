from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/your_database_name'
app.config['SECRET_KEY'] = 'your_secret_key'
mongo = PyMongo(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'


class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({'_id': user_id})
    user = User()
    user.id = user_id
    user.is_admin = user_data.get('is_admin', False)
    return user


from blueprints.auth import auth_bp
from blueprints.admin import admin_bp
from blueprints.user import user_bp

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
