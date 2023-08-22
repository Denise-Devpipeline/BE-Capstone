from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_passport_hash
from db import db
from models.customer import Customer
from controllers import customer_controller


customer_routes = Blueprint('customer_routes', __name__)

@customer_routes.route('/customers/add', method=["POST"])
def add_customer():
    return customer_controller.add_customer(request)

@customer_routes.route('/customers/update/<id>', method=["PATCH"])
def update_customer(id):
    return customer_controller.update_customer(request, id)

@customer_routes.route('/customers/decativate/<id>', method=["PATCH"])
def deactivate_customer(id):
    return customer_controller.deactivate_customer(request, id)

@customer_routes.route('/customers/activate/<id>', method=["PATCH"])
def activate_customer(id):
    return customer_controller.activate_customer(request, id)

@customer_routes.route('/customers/delete/<id>', method=["DELETE"]) 
def delete_customer(id):
    return customer_controller.delete_customer(request, id)
    
 

    
    