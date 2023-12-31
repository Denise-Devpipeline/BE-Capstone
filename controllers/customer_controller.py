from flask import request, jsonify, Blueprint
from db import db
from models.customer import Customer, customer_schema, customers_schema
from util.authentication import decoded_token
from util.hashing import generate_passport_hash
from util.reflection import populate_object

customer_controller = Blueprint('customer_controller', __name__)

@customer_controller.route('/customers/get_all_customers', methods=["GET"])
def get_all_customers():
    auth_token = request.headers.get('Authorization')
    if not auth_token:
        return jsonify({"Message": "Authorization token missing"}), 401
    
    decoded_token = decoded_token(auth_token)
    
    if not decoded_token:
        return jsonify({"Message": "Invalid token"}), 401
    
    if decoded_token['role'] != 'event_planner':
        return jsonify({"Message": "Unauthorized"}), 403
    
    planner_id = decoded_token['user_id']
    customers = db.session.query(Customer).filter(Customer.planner_id == planner_id).all()

    if not customers:
        return jsonify({"Message": "No customers found"}), 404
    
    return jsonify(customers_schema.dump(customers)), 200

# CREATE
def add_customer():
   req_data = request.form if request.form else request.json 

   if not req_data:
       return jsonify("Please enter all required fields."), 401
   
   new_customer = Customer.new_customer()
   populate_object(new_customer, req_data)

   new_customer.password = generate_passport_hash(new_customer.password). decode('utf8')

   db.session.add(new_customer)
   db.session.commit()

   return jsonify({"Message": "Customer added", "customer": customer_schema.dump(new_customer)}), 200
   
#UPDATE    # I want the customer to be able to update their Customer Table information only.
def update_customer(id):
    req_data = request.form if request.form else request.json
    existing_customer = db.session.query(Customer).filter(Customer.cust_id == id).first()

    if not existing_customer:
        return jsonify("Customer not found"), 404
    
    auth_token = request.headers.get('Authorization')
    if not auth_token:
        return jsonify("Authorization token missing"), 401
    
    decoded_token = decoded_token(auth_token)
    if not decoded_token:
        return jsonify("Invalid token"), 401
    
    if decoded_token['cust_id'] != existing_customer.cust_id:
        return jsonify("Unauthorized"), 403

    existing_customer.first_name = req_data.get('first_name', existing_customer.first_name)
    existing_customer.last_name = req_data.get('last_name', existing_customer.last_name)
    existing_customer.email = req_data.get('email', existing_customer.email)
    existing_customer.phone = req_data.get('phone', existing_customer.phone)

    db.session.commit()

    return jsonify({"Message": "Customer information Updated"}), 200


# DEACTIVATE  I wanted to prevent them from deactivating themselves but not sure that was accomplished here. 
@customer_controller.route('/customers/deactivate/<id>', methods=["PATCH"])
def deactivate_customer(id):
    customer = db.session.query(Customer).filter(Customer.cust_id == id).first()

    if not customer:
        return jsonify("Customer not found"), 404
    
    auth_token = request.headers.get('Authorization')
    if not auth_token:
        return jsonify("Authorization token missing"), 401
    
    decoded_token = decoded_token(auth_token)
    if not decoded_token:
        return jsonify("Invalid token"), 401
    
    if decoded_token['cust_id'] != customer.cust_id:
        return jsonify("Unauthorized"), 403
    
    if decoded_token['role'] != 'event_planner':
        return jsonify("Unauthorized to change status"), 403
    
    customer.active=False
    db.session.commit()

    return jsonify ({"Message": "Customer Deactivated"}), 200


# ACTIVATE  If the Customer is deactivated by the Event Planner then Customer should not be able to activate themselves.  
#Event Planner is the only one allowed to activate and deactivate a Customer.
@customer_controller.route('/customers/activate/<id>', methods=["PATCH"])
def activate_customer(id):
    customer = db.sesstion.query(Customer).filter(Customer.cust_id == id).first()

    if not customer:
        return jsonify("Customer not found"), 404
    
    auth_token = request.headers.get('Authorization')
    if not auth_token:
        return jsonify("Authorization token missing"), 401
    
    decoded_token = decoded_token(auth_token)
    if not decoded_token:
        return jsonify("Invalid token"), 401
    
    if decoded_token['cust_id'] != customer.cust_id:
        return jsonify("Unauthorized"), 403
    
    if decoded_token['role'] != 'event_planner':
        return jsonify("Unauthorized to change status"), 403
    
    customer.active=True
    db.session.commit()

    return jsonify ({"Message": "Customer Activated"}), 200


# DELETE Customer should not be allowed to Delete themselves.  Only the Event Planner can delete customer.
@customer_controller.route('/customers/delete/<id>', methods=["DELETE"]) 
def delete_customer(id):
    customer = db.sesstion.query(Customer).filter(Customer.cust_id == id).first()

    if not customer:
        return jsonify("Customer not found"), 404
    
    auth_token = request.headers.get('Authorization')
    if not auth_token:
        return jsonify("Authorization token missing"), 401
    
    decoded_token = decoded_token(auth_token)
    if not decoded_token:
        return jsonify("Invalid token"), 401
    
    if decoded_token['cust_id'] != customer.cust_id:
        return jsonify("Unauthorized"), 403
    
    if decoded_token['role'] != 'event_planner':
        return jsonify("Unauthorized to Delete"), 403
    
    db.session.delete(customer)
    db.session.commit()

    return jsonify ({"Message": "Customer Deleted"}), 200
