def calculate(text_input):
    for char in text_input:
        if not char.isalnum():
            if char == "+":
                x = text_input.split("+")
                return int(x[0]) + int(x[-1])
            elif char == "-":
                x = text_input.split("-")
                return int(x[0]) - int(x[-1])
            elif char == "*":
                x = text_input.split("*")
                return int(x[0]) * int(x[-1])
            elif char == "/":
                x = text_input.split("/")
                return int(x[0]) / int(x[-1])
            elif char == "~":
                x = text_input.split("~")
                return [int(x[0]) // int(x[-1]), int(x[0]) % int(x[-1])]
    return "ERROR"


print("Welcome to the Python calculator!")
rep = int(input("How many calculations do you want to do?"))

for _ in range(rep):
    user_input = input("What do you want to calculate? ")
    result = calculate(user_input)
    if "~" in user_input:
        print(f"The answer is {result[0]}\nThe remainder is {result[1]}")
    else:
        print(f"The answer is {result}")



