import re

def remove_bmw(string):
    if type(string) == str:
        new_string = re.sub('[bmw]', '', string, flags=re.IGNORECASE) #re.IGNORCASE is ignore letter case
        return new_string
    else:
        return TypeError("This program only works for text.")

print(remove_bmw("bmwvolvoBMW"))