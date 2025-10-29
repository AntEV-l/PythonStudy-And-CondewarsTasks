expression = input().replace("+"," + ").replace("-", " - ").split()
print(expression)
result = int(expression[0])
for i in range(1, len(expression), 2):
    operator = expression[i]
    number = int(expression[i + 1])
    if operator == '+':
        result += number
    elif operator == '-':
        result -= number