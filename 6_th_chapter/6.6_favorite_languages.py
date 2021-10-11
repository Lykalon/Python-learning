favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
auditory = ['jen', 'phil', 'janette', 'tom', 'edward']
for name in auditory:
    if name in favorite_languages.keys():
        print(f'{name.title()}, thank you for taking the poll.')
    else:
        print(f'{name.title()}, please take our poll.')
