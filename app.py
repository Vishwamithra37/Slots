from flask import  Flask
from admin import admin_page
app = Flask(__name__)

app.register_Blueprint(admin_page,url_prefix="admin")

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)