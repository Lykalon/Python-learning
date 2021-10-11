rivers = {
    'nile': 'egyrt',
    'volga': 'russia',
    'amazon': 'brazil',
    }
for name, country in rivers.items():
    print(f'The {name.title()} runs through {country.title()}')
for name1 in rivers.keys():
    print(name1.title())
for country1 in rivers.values():
    print(country1.title())
