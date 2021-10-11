sandwich_orders = ['tuna', 'classic', 'vegan', 'sporty']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'We made {current_sandwich} sandwich for you')
    finished_sandwiches.append(current_sandwich)
    
print('\nSandwiches we made today:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
