numbers = [value for value in range(3, 31)]
answer = []
for value in numbers:
    if value % 3 == 0:
        answer.append(value)
print(answer)
first_three = answer[:3]
last_three = answer[-3:]
count = len(answer) // 2
middle_three = answer[count - 1: count + 2]
print(f'The first three items in the list are: {first_three}')
print(f'Three items from the middle of the list are: {middle_three}')
print(f'The last three items in the list: {last_three}')
