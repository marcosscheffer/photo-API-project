from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from ..extensions import jwt
from ..services.auth_service import get_admin, get_user_by_email, gen_tokens, register_user, get_user_by_id
from ..schemas.user_schemas import LoginUserSchema, RegisterUserSchema

bp = Blueprint("auth", __name__)
BLOCKLIST = set()

@jwt.token_in_blocklist_loader
def is_token_revoked(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST

@jwt.additional_claims_loader
def add_claims(identity):
    user = get_admin(identity)
    return user

@bp.route("/login", methods=['POST'])
def login():
    data = request.get_json() or {}
    lus = LoginUserSchema()
    validate = lus.validate(data)
    if validate:
        return validate, 400
    
    user = get_user_by_email(data["email"])
    if not user or user.verify_password(data["password"]):
        return jsonify("Email or password is incorrect"), 401
    
    tokens = gen_tokens(user.id)
    return jsonify(tokens), 200

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    rus = RegisterUserSchema()
    validate = rus.validate(data)
    if validate:
        return validate, 400
    
    register = register_user(data["username"], data["email"], data["password"])
    return jsonify(register), 201

@bp.route("/refresh", methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    new_access = gen_tokens(user_id, False)
    return jsonify(new_access), 200

@bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jti = get_jwt["jti"]
    BLOCKLIST.add(jti)
    return jsonify("logout successfully"), 200

@bp.route("/me", methods=["POST"])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    if not user:
        return jsonify("Not found"), 404
    
    return jsonify({"id": user.id,
                    "username": user.username,
                    "email": user.email
                    })
    
    


    

    
