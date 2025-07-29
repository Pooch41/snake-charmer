def print_multiplication_table(n):
  print('  ', end=' ')

  for i in range(1, n+1):
    print(f"{i:2d}", end='  ')
  print()

  for i in range(1, n+1):
    print(i, end=' ')

    for j in range(1, n+1):
      product = i * j

      print(f"{product:3d}", end=' ')
    print()

def print_line(len):
    for j in range(1, len):
        print(j, end=' ')
    print()

def print_triangle(size):
    for i in range(2, size + 2):
        print_line(i)
    for i in range(size, 1, -1):
        print_line(i)



def get_user_input():
    while True:
        n = int(input("Please enter a number: "))

        if n == -1:
            print("Bye!")
            break

        cmd = input("Please enter a command(triangle / mp): ")

        if cmd == "triangle":
            print_triangle(n)
        elif cmd == "mp":
            print_multiplication_table(n)
        else:
            print("Invalid command")


get_user_input()


