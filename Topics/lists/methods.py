numbers = [1,2,3,4,5]
number1 = list(range(1,6))
number2 = list()
names = ["bob", "dod", "eoe"]
#
bob, dod, eoe = names
#for
for item in numbers:
    print(item, end=" ")
#slice
num1_3 = numbers[:4]
num3_ = numbers[4:]
print(num1_3, num3_)
#methods
number1.append(3) #append item in the end of list
number1.insert(2, 4) #append item by index, first param - index
number1.extend([6,7]) #append group of item
#removing