def array(string):
    if len(string) < 3 or string == '':
        return None
    return string[1:-1].replace(",", " ").strip()
print(array(''))

