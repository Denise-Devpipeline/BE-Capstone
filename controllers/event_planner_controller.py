from flask import request, Response, jsonify
from flask_bcrypt import generate_passport_hash

from db import db
from models.event_planner import EventPlanner, event_planner_schema, event_planners_schema
from util.reflection import populate_object

# A planner should be able to add, update, activate, deactivate themselves.  
# They should be able to view all Customers. 
# Not be able to delete themselves.
# Planners should be able to view everything on Event Services and on Venue tables.


#ADD 
def add_event_planner():
    req_data = request.form if request.form else request.json
    if not req_data:
        return jsonify("Please enter all the required fields"), 401

    new_event_planner= EventPlanner.new_event_planner()

    populate_object(new_event_planner, req_data)

    new_event_planner.password = generate_passport_hash(new_event_planner.password).decode('utf8')

    db.session.add(new_event_planner)
    db.session.commit()

    return jsonify({"Message": "Event Planner Added", "event_planner": event_planner_schema.dump(new_event_planner)}), 200

# READ  ********The Event Planner has access to see ALL Event Planners. 
def get_all_event_planners():
    event_planners = db.session.query(EventPlanner.active == True).all()

    return jsonify(event_planners_schema.dump(event_planners)), 200

    
def get_all_event_planners_by_id(id):
    event_planner = db.session.query(EventPlanner).filter(EventPlanner.planner_id == id).first()

    if not event_planner:
        return jsonify("Event planner not found"), 404
    return jsonify(event_planner_schema.dump(event_planner)), 200


# UPDATE
def update_event_planner(id):
    req_data = request.form if request.form else request.json

    existing_event_planner = db.session.query(EventPlanner).filter(EventPlanner.planner_id == id).first()
    if not existing_event_planner:
        return jsonify("Event Planner not found"), 404
    
    populate_object(existing_event_planner, req_data)

    db.session.commit()

    return jsonify({"Message": "Event Planner information Updated"}), 200


# DEACTIVATE 
def deactivate_event_planner(id):
    event_planner = db.session.query(EventPlanner).filter(EventPlanner.planner_id == id).first()

    if not event_planner:
        return jsonify("Event Planner not found"), 404
    
    event_planner.active = False

    db.session.commit()

    return jsonify ({"Message": "Event Planner Deactivated"}), 200


#ACTIVATE
def deactivate_event_planner(id):
    event_planner = db.session.query(EventPlanner).filter(EventPlanner.planner_id == id).first()

    if not event_planner:
        return jsonify("Event Planner not found"), 404
    
    event_planner.active = True

    db.session.commit()

    return jsonify ({"Message": "Event Planner Activated"}), 200


# DELETE
def delete_event_planner(id):
  event_planner = db.session.query(EventPlanner).filter(EventPlanner.planner_id == id).first()

  if not event_planner:
      return jsonify("Event Planner not found"), 404
  
  db.session.delete(event_planner)
  db.session.commit()
  
  return jsonify ({"Message": "Event Planner Deleted"}), 200