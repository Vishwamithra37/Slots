from flask import  Flask
from ADMIN_BP_LEELA.admin import admin_page
from USER_BP_NAVYA.users import users_bp

app = Flask(__name__)

app.register_blueprint(admin_page)
app.register_blueprint(users_bp)

@app.route('/')
def hello():
    return 'Hello World!'
#trail 
if __name__ == '__main__':
    app.run(debug=True)