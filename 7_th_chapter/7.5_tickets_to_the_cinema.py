prompt = "\nPlease enter your age here to know your price:"
prompt += "\nEnter 'quit' to end the program.\n"
message = ""
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        if 0 < int(message) < 3:
            price = 0
        elif 3 <= int(message) <= 12:
            price = 10
        elif int(message) > 12:
            price = 15
        else:
            price = -1;
            print("Wrong data. Try again!")
        if price > 0:
            print(f"For {message} years price is {price}")
