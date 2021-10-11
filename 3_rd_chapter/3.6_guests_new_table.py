guests = ['Victoria', 'Nikita', 'Elena', 'Nastya', 'Mariya']
for name in guests:
    print(f'Dear {name},\nI wanna see you on my Birthday-party 2morrow\n')
print('\nNow I have big table, greetings for Andrei, Kira and Misha!\n\n')
guests.insert(0, 'Andrei')
guests.insert(len(guests) // 2, 'Kira')
guests.append('Misha')
for name in guests:
    print(f'Dear {name},\nI wanna see you on my Birthday-party 2morrow\n')
