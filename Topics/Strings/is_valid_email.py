pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
import re
def is_valid_email(email):
    if re.match(pattern, email):
        return True
    else:
        return False

print(is_valid_email("pesmail.ru"))
