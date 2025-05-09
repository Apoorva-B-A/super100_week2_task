# task2_email_validation.py

import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Examples
print(is_valid_email("user@domain.com"))  # True
print(is_valid_email("user@domain"))      # False
