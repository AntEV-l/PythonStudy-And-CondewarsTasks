value = int(input())

res = [[1 if x == y else 0 for x in range(value)  ] for y in range(value)]
for row in res:
    print(*row)