from flask import request, jsonify, Blueprint
from flask import Flask
from flask_bcrypt import Bcrypt
from models import User
from lib.authenticate import auth
from db import db


app = Flask(__name__)
bcrypt = Bcrypt(app)



auth_routes = Blueprint('auth_routes', __name__)

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


@app.route('/login', methods=["POST"])
def login():
    data = request.json
    email = data.get('email') 
    password = data.get('password')

    hashed_password = bcrypt.generate_password_hash(8888).decode("utf-8")

    user = User(email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()

  
@auth_routes.route('/profile', methods=['GET'])
def get_profile():
    user_id = decode_token(request.headers.get('Authorization'))
    user = User.query.get(user_id)
    return jsonify({"username": user.username, "email": user.email}), 200
