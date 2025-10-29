int_input = int(input("Enter a number: "))
list_output = [ x for x in range(1,int_input+1) if int_input % x == 0 ]
print(list_output)