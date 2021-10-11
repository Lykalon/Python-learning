elem = ['dodge', 'pineapple', 'elena', 'earrings', 'cat']
elem_really = ['dodge', 'pineapple', 'elena', 'earrings', 'cat']
alternative = ['audi', 'apple', 'irina', 'ring', 'dog']
names = ['car', 'fruit', 'friend', 'accessory', 'pet']
for value in range(0, 5):
    print(f"Is {names[value]} == '{elem[value]}'? I predict True.")
    print(elem[value] == elem_really[value])

    print(f"\nIs {names[value]} == '{alternative[value]}'? I predict False.")
    print(elem[value] == alternative[value])
    print('\n\n')
