string1 = 'Hello, world!'
string2 = 'Hello, my friend!'
string3 = 'Hello, world!'

print('We have 3 strings. 2 of them are equal:')
print(f'First: {string1}')
print(f'Second: {string2}')
print(f'Third: {string3}')
print('First == Second: ', string1 == string2)
print('First == Third: ', string1 == string3, '\n')

rus = 'usiki'
eng = 'whiskers'
name = 'Usiki'
print("I have a cat. It's calls Usiki\n")
print('Usiki == Whiskers: ', name.lower() == eng)
print('Usiki == usiki: ', name.lower() == rus, '\n')

my_age = 25
dimas_age = 13
print('В нашей стране возраст молодежи считается от 14 до 30 лет.\n'
      'Давайте проверим, относитесь вы к молодежи, или нет.')
print('Мой возраст: ', my_age)
if 14 <= my_age <= 30:
    print('В нашей стране я отношусь к молодежи\n')
else:
    print('В нашей стране я не отношусь к молодежи\n')
print('Возраст Дмитрия: ', dimas_age)
if 14 <= dimas_age <= 30:
    print('В нашей стране Дмитрий отноcится к молодежи\n')
else:
    print('В нашей стране Дмитрий не относится к молодежи\n')

print('В нашей стране возраст молодежи считается от 14 до 30 лет.\n'
      'Давайте проверим, относитесь вы к молодежи, или нет.')
print('Мой возраст: ', my_age)
if 14 <= my_age and my_age <= 30:
    print('В нашей стране я отношусь к молодежи\n')
else:
    print('В нашей стране я не отношусь к молодежи\n')
print('Возраст Дмитрия: ', dimas_age)
if 14 <= dimas_age and dimas_age <= 30:
    print('В нашей стране Дмитрий относится к молодежи\n')
else:
    print('В нашей стране Дмитрий не относится к молодежи\n')

users_signed_up = ['andrey', 'john', 'alex', 'victoriya', 'elena']
new_user1 = 'John'
new_user2 = 'George'

print(f'Hello, {new_user1.title()}!')
if new_user1.lower() in users_signed_up:
    print('Oops, you need to create new account name. This name already taken!\n')
else:
    print('You are welcome to the site!\n')

print(f'Hello, {new_user2.title()}!')
if new_user2.lower() in users_signed_up:
    print('Oops, you need to create new account name. This name already taken!\n')
else:
    print('You are welcome to the site!\n')


users_signed_up1 = ['andrey', 'john', 'alex', 'victoriya', 'elena']
new_user_1 = 'Alex'
new_user_2 = 'Sergei'

print(f'Hello, {new_user_1.title()}!')
if new_user_1.lower() not in users_signed_up1:
    print('You are welcome to the site!\n')
else:
    print('Oops, you need to create new account name. This name already taken!\n')

print(f'Hello, {new_user_2.title()}!')
if new_user_2.lower() not in users_signed_up1:
    print('You are welcome to the site!\n')
else:
    print('Oops, you need to create new account name. This name already taken!\n')
