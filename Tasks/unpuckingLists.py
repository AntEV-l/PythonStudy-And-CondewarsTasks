value = int(input())
result = []
for item in range(value):
    r = []
    for j in range(value):
        if j == value - 1:
            r.append(5)
        else:
            r.append(1)
    result.append(r)

for inner_list in result:
    print(' '.join(map(str, inner_list)))



