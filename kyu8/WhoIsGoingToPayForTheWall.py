# https://www.codewars.com/kata/58bf9bd943fadb2a980000a7/train/python
def who_is_paying(name):
    if len(name) < 3:
        return [name]
    return list([name, name[0:2]])
print(who_is_paying("I"))