import database.interact as interact
import utils.password as password_utils

def user_login(user):
    if not user.email or not user.password:
        return {"error": "Email and password are required."}, 400

    existing_user = interact.Users().show(user.email)
    if not existing_user:
        return {"error": "User not found."}, 404

    hashed_password = existing_user["password"]
    if not password_utils.verify_password(user.password, hashed_password):
        return {"error": "Invalid password."}, 401

    return {
        "email": existing_user["email"],
        "password": existing_user["password"],
    }, 201