# task1.py

# Initial list of users
users = [
    {"Id": 1, "name": "Alice", "email": "alice@example.com"},
    {"Id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Function to add a user
def add_user(user_id, name, email):
    for user in users:
        if user["Id"] == user_id:
            return "User ID already exists!"
    users.append({"Id": user_id, "name": name, "email": email})
    return "User added successfully."

# Function to retrieve user by ID
def get_user(user_id):
    for user in users:
        if user["Id"] == user_id:
            return user
    return "User not found."

# Function to update user by ID
def update_user(user_id, name=None, email=None):
    for user in users:
        if user["Id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            return "User updated."
    return "User not found."

# Function to delete user by ID
def delete_user(user_id):
    for user in users:
        if user["Id"] == user_id:
            users.remove(user)
            return "User deleted."
    return "User not found."

# ----------- TEST CASES -----------
print("Initial Users:", users)

# Add a user
print(add_user(3, "Charlie", "charlie@example.com"))

# Retrieve new user
print(get_user(3))
