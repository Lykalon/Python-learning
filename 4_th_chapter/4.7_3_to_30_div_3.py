numbers = [value for value in range(3, 31)]
answer = []
for value in numbers:
    if value % 3 == 0:            # % - это деление с остатком, (value % 3 == 0) -
        answer.append(value)      # это "Если остаток 'value' при делении на 3 равен 0"
print(answer)
