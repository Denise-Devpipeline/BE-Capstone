from flask import request, Blueprint
from db import db
from controllers.customer_controller import customer_controller


customer_routes = Blueprint('customer_routes', __name__)

customer_routes.route('/customers/get_all_customers', methods=["GET"])
(customer_controller.get_all_customer)

customer_routes.route('/customers/add', methods=["POST"])
(customer_controller.add_customer)

customer_routes.route('/customers/update', methods=["PATCH"])
(customer_controller.update_customer)

customer_routes.route('/customers/deactivate', methods=["PATCH"])
(customer_controller.deactivate_customer)

customer_routes.route('/customers/activate', methods=["PATCH"])
(customer_controller.activate_customer)

customer_routes.route('/customers/delete', methods=["DELETE"])
(customer_controller.delete_customer)


# @customer_routes.route('/customers/get_all_customers', method=["GET"])   
# def get_all_customer():
#     return customer_controller.get_all_customers(request)

# @customer_routes.route('/customers/add', method=["POST"])
# def add_customer():
#     return customer_controller.add_customer(request)

# @customer_routes.route('/customers/update/<id>', method=["PATCH"])
# def update_customer(id):
#     return customer_controller.update_customer(request, id)

# @customer_routes.route('/customers/decativate/<id>', method=["PATCH"])
# def deactivate_customer(id):
#     return customer_controller.deactivate_customer(request, id)

# @customer_routes.route('/customers/activate/<id>', method=["PATCH"])
# def activate_customer(id):
#     return customer_controller.activate_customer(request, id)

# @customer_routes.route('/customers/delete/<id>', method=["DELETE"]) 
# def delete_customer(id):
#     return customer_controller.delete_customer(request, id)
    
 

    
    