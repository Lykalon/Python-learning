prompt = "\nWhat do you wanna add to pizza? Enter topping here:"
prompt += "\nEnter 'quit' to end the program.\n"
message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(f"{message} added to order")
