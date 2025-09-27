def remove_every_other(my_list):
    del my_list[1::2] #Deleting items from a list by index or slice:
    return my_list
print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
