# find
text = "Hello This is Python"
print(text.find("")) #return index or -1 from left to right
print(text.rfind("Hello")) #from right to left
print(text.index("is")) #return index of element or ValueError substring not found
#reverse and slice
text = "Python Programming"
print(text[0:6])    # "Python"
print(text[7:])     # "Programming"
print(text[:6])     # "Python"
print(text[::2])    # "Pto rgamn" (every second char)
print(text[::-1])   # "gnimmargorP nohtyP" (reverse)
#changing
# delete of space
print(text.strip())
print(text.lstrip())
print(text.rstrip())
# replace
textTwo = text.replace("Python", "JavaScript")
print(textTwo)
#create a list
textList = text.split(" ")
#create a string
text = " ".join(textList)
print(text)
#
print(text.upper())
print(text.lower())
print(text.capitalize()) #The first char Upper other lower
print(text.title()) #The first char of all words - Upper
print(text.swapcase())
# alignment
print("hello".ljust(10, "-"))  # "hello-----"
print("hello".rjust(10, "-"))  # "-----hello"
print("hello".center(11, "-")) # "---hello---"
#
path = r"C:\Users\Name\Documents"  # raw strings - ignor symbols
print(path)  # "C:\Users\Name\Documents"