from flask import jsonify, request, Blueprint
from flask_bcrypt import check_password_hash

from datetime import datetime, timedelta

from models.customer import Customer
from models.event_planner import EventPlanner
from models.event_svcs import EventSvcs
from models.planner_event_xref import PlannerEventXref
from models.venue import Venue
from models.auth_tokens import AuthTokens, auth_token_schema

from db import db

##### I think I need to have Customers and Event Planners sign in, do I need to have do different Auth tokens for each? (auth token add)


def auth_token_add():
    token_request = request.json
    email = token_request.get('email')
    password = token_request.get('password')
    expire = datetime.now() + timedelta(hours=12)
    user_data = db.session.query(Customer).filter(Customer.email == email).filter(Customer.active).first()

    if not email or not password or not user_data:
        return jsonify({"message": "Invalid Login"}), 401

    existing_tokens = db.session.query(AuthTokens).filter(AuthTokens.user_id == user_data.user_id).all()
    if existing_tokens:
        for token in existing_tokens:
            if token.expiration < datetime.now():
                db.session.delete(token)

    new_token = AuthTokens(user_data.user_id, expire)
    db.session.add(new_token)
    db.session.commit()

    return jsonify({"message": {"auth_token": auth_token_schema.dump(new_token)}})
