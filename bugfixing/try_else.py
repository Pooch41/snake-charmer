try:
    a = int(123)
    print("YAY!")
except ValueError:
    program_survived = False
    print("crash")
else:
    program_survived = True