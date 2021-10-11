vacation_database = {}
polling_status = True

while polling_status:
    name = input("\nWhat is your name?\n")
    place = input("Which country you want to travel to while on vacation?\n")
    vacation_database[name] = place

    repeat = input("Would you like to let another person respond? (y/n)\n")
    if repeat == 'n':
        polling_status = False

print("\n--- Poll results ---")
for name, place in vacation_database.items():
    print(f"{name} would like to go to the {place} on vacation")
