def city_country(city_f, country_f):
    formatted = f"{city_f}, {country_f}"
    return formatted.title()


while True:
    print("Enter 'q' at any time for exit")
    city = input("Enter city: ")
    if city == 'q':
        break
    country = input("Enter country for city: ")
    if country == 'q':
        break
    print(f"\nFormatted string : {city_country(city, country)}\n")
