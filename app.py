from flask import  Flask
from admin import admin_page
app = Flask(__name__)

app.register_blueprint(admin_page)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)