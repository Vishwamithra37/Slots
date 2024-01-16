from flask import  Flask
from ADMIN_API_BP_LE.routes import admin_page
#from USERS_API_BP_NS.users import users_bp

app = Flask(__name__)

app.register_blueprint(admin_page)
#app.register_blueprint(users_bp)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)