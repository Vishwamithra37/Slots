from flask import Flask
from SLOTS_API_BP_DS.slot_booking_blueprint import slots_bp

app = Flask(__name__)
app.register_blueprint(slots_bp, url_prefix='/slot_routes')

if __name__ == '__main__':
    app.run(debug=True)
