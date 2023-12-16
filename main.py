from flask import Flask,url_for
from users import users_bp
from admin import admin_bp



app = Flask(__name__)
app.secret_key="Hopethisworks"


app.register_blueprint(users_bp, url_prefix='/users_rel_routes')
app.register_blueprint(admin_bp, url_prefix='/admin_rel_routes')


@app.route('/route_name', methods=['POST'])
def method():
    return "welcome"

if __name__ == '__main__':
    app.run(debug=True)