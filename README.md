# Slots
Slot booking Application API

# Pre-requistors
1) Database - Mongodb

# Instructions 

1) install venv 
   ~~~sh
   python -m venv project_Slotzz
   . project_Slotzz/Scripts/activate
   
   ~~~
2) requirements.txt
   ~~~sh
   pip install -r requirements.txt
   
   ~~~
3) Running application
    ~~~sh
    python app.py
    ~~~
    
# Instructions for Swagger

# 1) Installation of swagger:
~~~sh
pip install flask-swagger
~~~
# 2) After installing import swagger in app.py:
~~~sh
from flask_swagger import swagger
~~~
then create a route in app.py as follows:
~~~sh 
@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)
~~~
run the app.py file.

# 3) Opening swagger documentation:
 1.You can open the Swagger documentation in a web browser by accessing the Swagger via a specific URL.(/spec) which we mentioned in our app.py
 
 2.Now u need to COPY that content in the web browser which displayed right after accesing the url 
 
 3.PASTE it in ONLINE SWAGGER EDITOR (Converting json to YAML)
 
 4.Bingo.You can see the routes and inputs that routes expecting and also the type of input
 

