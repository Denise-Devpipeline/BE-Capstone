from flask import jsonify, request, Blueprint
from flask_bcrypt import check_password_hash

from datetime import datetime, timedelta

from models.customer import Customer
from models.event_planner import EventPlanner
from models.event_svcs import EventSvcs
from models.planner_event_xref import PlannerEventXref
from models.venue import Venue
from models.auth_token import AuthToken, auth_token_schema

from db import db


def auth_token_add():
    token_request = request.json
    email = token_request.get('email')
    password = token_request.get('password')
    expire = datetime.now() + timedelta(hours=12)
    user_data = db.session.query(Customer).filter(Customer.email == email).filter(Customer.active).first()
