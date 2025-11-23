import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$'
    return re.match(pattern, email)

email = input().strip()

if is_valid_email(email):
    print("OK")
else:
    print("WRONG")