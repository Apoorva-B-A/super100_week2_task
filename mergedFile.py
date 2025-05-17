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
# task2_email_validation.py

import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Examples
print(is_valid_email("user@domain.com"))  # True
print(is_valid_email("user@domain"))      # False
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
# beginner1_anagram.py

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
# beginner3_most_frequent.py

from collections import Counter

def most_frequent(lst):
    if not lst:
        return None
    count = Counter(lst)
    return count.most_common(1)[0][0]

print(most_frequent([1, 2, 2, 3, 3, 3, 4]))  # 3
# beginner2_prime.py

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False
