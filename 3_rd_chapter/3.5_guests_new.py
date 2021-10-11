guests = ['Victoria', 'Nikita', 'Elena', 'Nastya', 'Mariya']
for name in guests:
    print(f'Dear {name},\n\tI wanna see you on my Birthday-party 2morrow\n')
print('\nNikita will be removed...\n\n')
guests[1] = 'Andrei'
for name in guests:
    print(f'Dear {name},\n\tI wanna see you on my Birthday-party 2morrow\n')
