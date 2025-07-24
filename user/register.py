import database.interact as interact
import utils.password as password_utils

def user_register(user):
    if not user.email or not user.password or not user.name or not user.role:
        return {"error": "All fields are required."}, 400

    if interact.Users().show(user.email):
        return {"error": "Email already registered."}, 409

    hashed_password = password_utils.hash_password(user.password)
    success = interact.Users().insert(
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