from flask import request, Response, jsonify
from flask_bcrypt import generate_passport_hash

from db import db
from models.venue import Venue, venue_schema, venues_schema
from util.reflection import populate_object

#ADD To add Venue, there needs to be name, address, phone, email fields added to create.
def add_venue():
    req_data = request.form if request.form else request.json
    if not req_data:
        return jsonify("Please enter the required fields"), 401

    new_venue= Venue.new_venue()

    populate_object(new_venue, req_data)

    db.session.add(new_venue)
    db.session.commit()

    return jsonify(venue_schema.dump(new_venue)), 200

#READ Event Planners should be able to see all Venues.  How do I control what fields show up upon getting all the Venues?
def get_all_venues():
    venues = db.session.query(Venue).all()

    if not venues:
        return jsonify("No Venues found"), 404
    
    return jsonify(venues_schema.dump(venues)), 200

def get_venue_by_id(venue_id):
    venue = db.session.query(Venue).filter(Venue.venue_id == venue_id).all()

    if not venue:
        return jsonify("No venue found"), 404
    
    return jsonify(venue_schema.dump(venue)), 200


#UPDATE  The Customer can see venues but only the Event planner can make updates.
def update_venues(id):
    req_data = request.form if request.form else request.json
    existing_venue = db.session.query(Venue).filter(Venue.venue_id == id).first()

    if not existing_venue:
        return jsonify("Venue not found"), 404
    
    populate_object(existing_venue, req_data)
    db.session.commit()

    return jsonify("Venue information updated"), 200

#DEACTIVATED The Event Planner can deactivate a venue but the Customer cannot.
def deactivate_venue(id):
    venue = db.session.query(Venue).filter(Venue.venue_id == id).first()

    if not venue:
        return jsonify("Venue not found"), 404
    
    venue.active = False
    db.session.commit()

    return jsonify("Venue deactivated")

#ACTIVATED  The Event Planner can activate a venue but the Customer cannot.
def activate_venue(id):
    venue = db.session.query(Venue).filter(Venue.venue_id == id).first()

    if not venue:
        return jsonify("Venue not found"), 404
    
    venue.active = True
    db.session.commit()

    return jsonify("Venue activated")


#DELETE  The Event Planner can delete a venue but the Customer cannot.
def delete_venue(id):
    venue = db.session.query(Venue).filter(Venue.venue_id == id).first()

    if not venue:
        return jsonify("Venue not found"), 404
    
    db.session.delete(venue)
    db.session.commit()

    return jsonify("Venue deleted"), 200