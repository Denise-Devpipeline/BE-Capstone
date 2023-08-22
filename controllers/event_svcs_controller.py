from flask import Flask
from flask import request, Response, jsonify
from flask_bcrypt import generate_passport_hash

from db import db
from models.event_svcs import EventSvcs, event_service_schema, event_services_schema
from util.reflection import populate_object

from routes.event_svcs_routes import event_svcs_routes

app = Flask(__name__)
app.register_blueprint(event_svcs_routes)

if __name__ == '__main__':
    app.run()

#ADD To add Event Services, there needs to be Event date and Location fields added to create.
def add_event_services():
    req_data = request.form if request.form else request.json
    if not req_data:
        return jsonify("Please enter the required fields"), 401

    new_event_services= EventSvcs.new_event_services()

    populate_object(new_event_services, req_data)

    new_event_services.password = generate_passport_hash(new_event_services.password).decode('utf8')

    db.session.add(new_event_services)
    db.session.commit()

    return jsonify(event_service_schema.dump(new_event_services)), 200

#READ Event Planners should be able to grab their Customer events.
def get_event_by_planner_id(planner_id):
    event_services = db.session.query(EventSvcs).filter(EventSvcs.cust_id == planner_id).all()

    if not event_services:
        return jsonify("No event services found"), 404
    
    return jsonify(event_services_schema.dump(event_services)), 200


#UPDATE  The Customer can see event services but only the Event planner can make updates.
def update_event_service(id):
    req_data = request.form if request.form else request.json
    existing_event_service = db.session. query(EventSvcs).filter(EventSvcs.service_id == id).first()

    if not existing_event_service:
        return jsonify("Event not found"), 404
    
    populate_object(existing_event_service, req_data)
    db.session.commit()

    return jsonify("Event Services information updated"), 200

#DEACTIVATED The Event Planner can deactivate but the Customer cannot.
def deactivate_event_service(id):
    event_service = db.session.query(EventSvcs).filter(EventSvcs.service_id == id).first()

    if not event_service:
        return jsonify("Event not found"), 404
    
    event_service.active = False
    db.session.commit()

    return jsonify("Event Service deactivated")

#ACTIVATED  The Event Planner can activate but the Customer cannot.
def activate_event_service(id):
    event_service = db.session.query(EventSvcs).filter(EventSvcs.service_id == id).first()

    if not event_service:
        return jsonify("Event not found"), 404
    
    event_service.active = True
    db.session.commit()

    return jsonify("Event Service activated")


#DELETE  The Event Planner can delete but the Customer cannot.
def delete_event_service(id):
    event_service = db.session.query(EventSvcs).filter(EventSvcs.service_id == id).first()

    if not event_service:
        return jsonify("Event not found"), 404
    
    db.session.delete(event_service)
    db.session.commit()

    return jsonify("Event Service deleted"), 200

