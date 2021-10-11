number = input("How many people will be at the table?\nPlease, write a number: ")
number = int(number)
if number > 8:
    print("Sorry, you need to wait a vacant table.")
else:
    print("Your table is ready. Have a nice time!")
