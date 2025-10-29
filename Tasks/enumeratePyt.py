example = [-5,-4,-3,-2,-1,0,1,2,3,5]
for index, item in enumerate(example):
    if item < 0:
        example[index] = abs(item)

print(example)