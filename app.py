from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "HOME"


from controller import *
user_controller.register_route(app)
product_controller.register_route11(app)


app.run(debug=True)