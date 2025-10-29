a = [f'{i}*{j} = {i * j}'
     for i in range(1, 10)
     for j in range(1, 10)]


b = [[0,1,2,3,4], [50,60,70,80], [100, 200, 300]]
res = [x
       for row in b
       for x in row
       ]

M, N = 3, 4
matrix = [[x for x in range(M) ] for y in range(N)]

A = [[1,2,3], [4,5,6], [7,8,9]]
res_list = [[x ** 2 for x in row] for row  in A] # row link to A[0] and then the internal LC take the value ** 2

matrixTwo = [[row[i] for row in A] for i in range(len(A[0]))]
print(matrixTwo)