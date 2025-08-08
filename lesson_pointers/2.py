def mult_by_ten(number):
    return number * 10


func_dict = {   "absolute" : abs,
                "round" : round,
                "mult" : mult_by_ten
            }


number = float(input("Enter a number please: "))
user_choice = input("""What would you like to do with your number?
                     absolute = Print the absolute value.
                     round = Print the rounded value.
                     multiply = Multiply the number by 10.
                     """)

chosen_func = func_dict[user_choice]
print(chosen_func(number))
