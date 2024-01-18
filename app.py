
from flask import  Flask,render_template

from flask_cors import CORS
from flask_swagger import swagger



from ADMIN_BP_LEELA.admin import admin_page
from USER_BP_NAVYA.users import users_bp


app = Flask(__name__)
#CORS(app, resources={r"/users_rel_routes/*": {"origins": "http://localhost:3000"}})
CORS(app)
app.secret_key = "something"

app.register_blueprint(users_bp, url_prefix='/users_rel_routes')
app.register_blueprint(admin_page)



@app.route('/')
def hello():

    return render_template("index.html")

    return 'Hello World!'
#trail 

if __name__ == '__main__':
    app.run(debug=True)