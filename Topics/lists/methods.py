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
#adding
number1.append(3) #append item in the end of list
number1.insert(2, 4) #append item by index, first param - index
number1.extend([6,7]) #append group of item
#removing
list_Removing = [1,2,3,4,5]
list_Removing.remove(1) #[1,2,3,4] or if elem doest not foud - Value error
list_Removing.pop() #return an elem by index or last elem if you don't get an index
# list_Removing.clear() - remove all elements from list
my_list = [1,2,3,4,5]
my_list.remove(1) # delete the first occurrence item in list or ValueError
my_list.pop()  # delete last elem in return it. If pop has an argument, pop will delete item by index
del my_list[0] # del elem by index
my_list.clear() # del all elements from list
#search
my_list_research = [1,2,3,4,5]
my_list_research.index(2) #return index of elem if it in the list or Value Error
my_list_research.count(2) # amount of this item in list
#copy
my_list_for_copy = [1,2,3,4,5]
copyOne = my_list_for_copy.copy()
copyTwo = my_list_for_copy[:]
copyThree = list(my_list_for_copy)