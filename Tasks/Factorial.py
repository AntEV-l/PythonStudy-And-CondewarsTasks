n = int(input())

if n < 1 or n > 100:
    print("incorrect integer")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)