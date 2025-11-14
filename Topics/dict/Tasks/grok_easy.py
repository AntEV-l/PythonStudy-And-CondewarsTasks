fruits = {"apple": 1, "orange": 2,}
def add_fruit(key, value):
    fruits[key] = value
    return fruits
print(add_fruit("banana", 12))

def get_key(dicti, key):
    if dicti.get(key):
        return key
    else:
        return None

def check_key(dicti, key):
    return True if key in dicti else False
