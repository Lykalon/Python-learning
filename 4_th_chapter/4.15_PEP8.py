my_pizzas = ['peperoni', 'margarita', 'ananas']
friends_pizzas = my_pizzas[:]

my_pizzas.append('bacon')
friends_pizzas.append('mushrooms')

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's fovorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza.title())
