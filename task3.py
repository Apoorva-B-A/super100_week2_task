# task3_auth.py

import hashlib

users_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users_db:
        return "Username already exists."
    users_db[username] = hash_password(password)
    return "Created new user."

def login(username, password):
    hashed = hash_password(password)
    if users_db.get(username) == hashed:
        return "Login Successful"
    return "Invalid username or password"

# Examples
print(register("john", "mypassword"))     # Created new user
print(login("john", "mypassword"))        # Login Successful
