
def most_frequent_char(s):
    counted_chars = {}
    for char in s:
        if char in counted_chars:
            counted_chars[char] += 1
        else:
            counted_chars[char] = 1
    return max(counted_chars, key=counted_chars.get)
print(most_frequent_char("hello"))