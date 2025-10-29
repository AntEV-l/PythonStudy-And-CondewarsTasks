
def count_vowels(s):
    counter = 0
    s = s.lower()
    for item in s:
        if item in 'aeiou':
            counter += 1

    return counter if counter >= 1 else "not found"

print(count_vowels("hello world"))