value = int(input())
a = [[i]* value for i in range(value)]
for i in a:
    print(*i)