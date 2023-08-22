#Need help with the login - Kind of feeling like I've done this in auth_controller already.
#Missing some imports but need to verify file locations first.
from flask import request, jsonify, Blueprint
from models import User


login_routes = Blueprint('login_routes', __name__)

@login_routes.route('/auth/update', methods=["PUT"])
@auth_required
def update_user():
    return jsonify({"Message": "user information updated"}), 200

# @auth_routes.route('/login', methods=['POST'])
# def login():
#     req_data = request.json
#     email = req_data.get('email')
#     password = req_data.get('password')

#     user = User.query.filter_by(email=email).first()

#     if user and user.check_password(password):
#         token = generate_token(user_id)
#         return jsonify({"Token": "token"}), 200
#     else:
#         return jsonify({"Message": "Invalid Credentials"}), 401
    
  
# @auth_routes.route('/profile', methods=['GET'])
# @auth_required
# def get_profile():
#     user_id = decode_token(request.headers.get('Authorization'))
#     user = User.query.get(user_id)
#     return jsonify({"username": user.username, "email": user.email}), 200
