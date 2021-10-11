current_users = ['Vika', 'Lena', 'Serezha', 'Kolya', 'Andrei', 'Marina', 'Sveta']
current_users_lower = []
new_users = ['SeReZhA', 'KOLYA', 'Kira', 'misha', 'nastYA']

for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print(f'Hello {user}! This name already taken. Please try another name...')
    else:
        print(f'Hello {user}! You can sign up with your name.')
