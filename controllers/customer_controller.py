from flask import request, Response, jsonify
from flask_bcrypt import generate_passport_hash

from db import db
from models.customer import Customer, customer_schema, customers_schema
from util.reflection import populate_object


# CREATE

def update_user(id):
    req_data = request.form if request.form else request.json
    existing_user = db.session.query(Users).filter(Users.user_id == id).first()

    new_user = Users.new_user
    populate_object(existing_user, req_data)

    new_user.password = generate_passport_hash(new_user.password).decode('utf8')

    db.session.commit()

    return jsonify("Customer Created"), 200


def add_user():
    req_data = request.form if request.form else request.json

    if not req_data:
        return jsonify("Please enter all the required fields"), 401

    new_user = Users.new_user()

    populate_object(new_user, req_data)

    new_user.password = generate_passport_hash(new_user.password).decode('utf8')

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user)), 200

# READ


def get_all_active_customers(request):
    customers = db.session.query(Customer).filter(Customer.active == True).all()

    if not customers:
        return jsonify('No customer Exist'), 404

    else:
        return jsonify(customer_schema.dump(customers)), 200


def get_users_by_id(id):
    customer = db.session.query(Customer).filter(Customer.cust_id == id).first()

    if not customer:
        return jsonify("That customer does not exist"), 404

    else:
        return jsonify(customer_schema.dump(customer)), 200

# UPDATE


def update_customer(id):
    req_data = request.form if request.form else request.json
    existing_customer = db.session.query(Customer).filter(Customer.cust_id == id).first()
    populate_object(existing_customer, req_data)

    existing_customer.password = generate_password_hash(existing_customer.password).decode('utf8')

    db.session.commit()

    return jsonify('Customer Created'), 200

# DEACTIVATE/ACTIVATE

# DELETE
