import app.database.interact as database_interact
import app.utils.password as utils_password

def register(user):
    if not user.email or not user.password or not user.name or not user.role:
        return {"error": "All fields are required."}, 400

    if database_interact.user.show(user.email):
        return {"error": "Email already registered."}, 409

    hashed_password = utils_password.hash_password(user.password)
    success = database_interact.user.insert(
        user.name, user.email, hashed_password, user.role
    )

    if not success:
        return {"error": "Failed to insert user."}, 500

    return {
        "username": user.name,
        "email": user.email,
        "password": user.password,
        "role": user.role
    }, 201

def login(user):
    if not user.email or not user.password:
        return {"error": "Email and password are required."}, 400

    existing_user = database_interact.user.show(user.email)
    if not existing_user:
        return {"error": "User not found."}, 404

    hashed_password = existing_user["password"]
    if not utils_password.verify_password(user.password, hashed_password):
        return {"error": "Invalid password."}, 401

    return {
        "email": existing_user["email"],
        "password": existing_user["password"],
    }, 201