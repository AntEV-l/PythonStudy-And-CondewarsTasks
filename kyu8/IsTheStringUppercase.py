# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python
def is_uppercase(inp):
    # .upper() create a new string with symbol changes. No letters don't change
    return inp == inp.upper()

print(is_uppercase("hello I AM DONALD"))