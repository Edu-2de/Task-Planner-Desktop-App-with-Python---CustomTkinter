import json
import os

USER_FILE = "data/users.json"

def load_users():
    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def authenticate_user(username, password):
    users = load_users()
    return {"username": username, "password": password} in users

def register_user(username, password):
    users = load_users()
    if any(u["username"] == username for u in users):
        return False
    users.append({"username": username, "password": password})
    save_users(users)
    return True