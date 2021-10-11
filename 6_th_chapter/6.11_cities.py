cities = {
    'moscow': {
        'country': 'russia',
        'population': '20kk',
        'fact': 'I am living here',
        },
    'samara': {
        'country': 'russia',
        'population': '1,67kk',
        'fact': 'I lived here',
        },
    'kazan': {
        'country': 'russia',
        'population': '1,79kk',
        'fact': 'I was born here',
        },
    }

for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f"{city.title()} is based in {country.title()}. There is {population} citizens. And {fact}.")
