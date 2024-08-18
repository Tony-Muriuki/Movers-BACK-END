from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, unset_jwt_cookies
from .models import db, User

bp = Blueprint('auth', __name__)

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()  # Get JSON data from the request
    hashed_password = generate_password_hash(data['password'])  # Hash the password
    
    user = User(email=data['email'], password_hash=hashed_password, role=data['role'])  # Create the User object
    
    db.session.add(user)  # Add the user to the session
    db.session.commit()  # Commit the session to save the user in the database
    
    return jsonify({"msg": "User created"}), 201  # Return a success message with a 201 status code

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user and check_password_hash(user.password_hash, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token , role=user.role), 200
    
    return jsonify({"msg": "Bad email or password"}), 401

@bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({"msg": "Logout successful"})
    unset_jwt_cookies(response)
    return response, 200