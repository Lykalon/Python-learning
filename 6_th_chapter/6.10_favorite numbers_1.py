favorite_numbers = {
    'sergei': ['12', '20'],
    'vika': ['17', '1', '10'],
    'lena': ['10', '3'],
    'kolya': ['7'],
    'vadim': ['3', '5', '7'],
    }
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} 's favorite numbers are:")
    for number in numbers:
        print(f'\t{number}')
