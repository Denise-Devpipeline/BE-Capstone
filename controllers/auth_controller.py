from flask import jsonify, request, Blueprint
from flask_bcrypt import check_password_hash


from datetime import datetime, timedelta

from models.customer import Customer
from models.event_planner import EventPlanner
from models.auth_tokens import AuthTokens, auth_token_schema

from db import db

# from models.event_svcs import EventSvcs
# from models.venue import Venue
# from models.planner_event_xref import PlannerEventXref

##### I think I need to have Customers and Event Planners sign in, do I need to have do different Auth tokens for each? (auth token add)

auth = Blueprint('auth', __name__)

@auth.route('/auth/token', methods=['POST'])
def auth_token_add():
    token_request = request.json
    email = token_request.get('email')
    password = token_request.get('password')
    expire = datetime.now() + timedelta(hours=12)
    user_data = db.session.query(Customer).filter(Customer.email == email).filter(Customer.active).first()

    if not user_data:
        user_data = db.session.query(EventPlanner).filter(EventPlanner.email == email, Customer.active == True).first()

    if not email or not password or not user_data:
        return jsonify({"Message": "Invalid Login"}), 401
    
    if not check_password_hash(user_data.password, password):
        return jsonify({"Message": "Invalid Login"}), 401
    
    existing_tokens = db.session.query(AuthTokens).filter(AuthTokens.user_id == user_data.user_id).all()
    if existing_tokens:
        for token in existing_tokens:
            if token.expiration < datetime.now():
                db.session.delete(token)

    new_token = AuthTokens(user_data.user_id, expire)
    db.session.add(new_token)
    db.session.commit()

    token_data = auth_token_schema.dump(new_token)
    token_data['user_id'] = user_data.user_id
    token_data['role'] = 'customer' if isinstance(user_data, Customer) else 'event_planner'


    return jsonify({"Message": {"auth_token": token_data}}), 200
