from flask import Flask
from slot_booking_blueprint import slots_bp

app = Flask(__name__)
app.register_blueprint(slots_bp, url_prefix='/slot_routes')

if __name__ == '__main__':
    app.run(debug=True)
