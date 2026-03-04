import jwt
from datetime import datetime, timedelta

SECRET = "secretkey"

fake_db = {}

def register_user(username, password):
    fake_db[username] = password
    return {"message": "User created"}

def login_user(username, password):
    if fake_db.get(username) != password:
        return {"error": "Invalid credentials"}

    token = jwt.encode(
        {"user": username, "exp": datetime.utcnow() + timedelta(hours=1)},
        SECRET,
        algorithm="HS256"
    )

    return {"token": token}