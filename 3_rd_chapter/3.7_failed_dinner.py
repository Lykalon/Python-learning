import random

guests = ['Victoria', 'Nikita', 'Elena', 'Nastya', 'Mariya']
allowed = 2
for name in guests:
    print(f'Dear {name},\nI wanna see you on my Birthday-party 2morrow\n')
print('\nNow I have big table, greetings for Andrei, Kira and Misha!\n\n')
guests.insert(0, 'Andrei')
guests.insert(len(guests) // 2, 'Kira')
guests.append('Misha')
for name in guests:
    print(f'Dear {name},\nI wanna see you on my Birthday-party 2morrow\n')
print('\nSome troubles with table. Now I can have only 2 guests in my house!\n\n')
print('So, some invitations will be randomly canceled!\n\n')
for i in range(len(guests) - allowed):
    popped_guest = guests.pop(random.randint(0, len(guests) - 1))
    print(f'{popped_guest}, I am sorry about cancellation!')
print('\n')
for name in guests:
    print(f'Dear {name}, your invitations still valid!')
for i in range(len(guests)):
    del guests[0]
print('\n')
print(guests)
