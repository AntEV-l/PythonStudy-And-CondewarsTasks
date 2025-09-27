# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python
def remove_char(s):
    if len(s) < 2:
        return ""
    return s[1:len(s)-1]
print(remove_char('abc'))