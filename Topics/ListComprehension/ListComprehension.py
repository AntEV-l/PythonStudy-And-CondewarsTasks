N = 6
# a  = [0] * N
#
# for i in range(N):
#     a[i] = i ** 2
# print(a)

a = [x  ** 2 for x in range(N)]
print(a)

d_inp = input()
a = [int(d) for d in d_inp.split() if d.isdigit() ]
print(a)

