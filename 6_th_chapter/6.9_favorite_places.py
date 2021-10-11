favotite_places = {
    'vika': ['moscow', 'piter'],
    'serezha': ['samara'],
    'lena': ['piter', 'taganrog', 'kaliningrad'],
    }
for name, places in favotite_places.items():
    print('\n', name.title())
    for place in places:
        print(place.title())
