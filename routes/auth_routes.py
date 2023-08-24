from flask import request, jsonify, Blueprint
from flask_bcrypt import check_password_hash
from models import User
from lib.authenticate import auth, auth_with_return

################ STILL HAVE A WAYS TO GO ON THIS PAGE.  

auth_routes = Blueprint('auth_routes', __name__)

role_permissions = {
    "EventPlanner": ["manage_users", "view_event_svcs", "view_venue"], 
    "Customer": ["edit_profile"]
}

#base role going to be planner or just a user? 
login_info = []
for planner_id in planner_ids:
    config.base_roles(planner_id)

hashed_password = bcrypt.generate_password_hash('8888').decode('utf8')

@auth_routes.route('/auth/update', methods=["PUT"])
@auth
def update_user():
    return jsonify({"Message": "user information updated"}), 200

@auth_routes.route('/auth', methods=['POST'])
def auth_user():
    req_data = request.json
    email = req_data.get('email')
    password = req_data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        token = 'dsafdfasdfsad'#generate_token(user_id)
        return jsonify({"Token": "token"}), 200
    else:
        return jsonify({"Message": "Invalid Credentials"}), 401
    
  
# @auth_routes.route('/profile', methods=['GET'])
# @auth_required
# def get_profile():
#     user_id = decode_token(request.headers.get('Authorization'))
#     user = User.query.get(user_id)
#     return jsonify({"username": user.username, "email": user.email}), 200
