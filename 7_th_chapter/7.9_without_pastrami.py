sandwich_orders = ['tuna', 'pastrami', 'classic', 'pastrami', 'tuna', 'vegan', 'sporty', 'pastrami']
finished_sandwiches = []
print("Oh, sorry! We don't have pastrami sandwiches.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'We made {current_sandwich} sandwich for you.')
    finished_sandwiches.append(current_sandwich)

print('\nSandwiches we made today:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
