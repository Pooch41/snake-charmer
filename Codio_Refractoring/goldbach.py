LOWEST_PRIME = 2
LOWEST_GOLDBACH = 4


def is_prime(n):
    """return if n is prime"""
    x = LOWEST_PRIME
    for i in range(LOWEST_GOLDBACH, n):
        if n % x == 0:
            return False
        x += 1
    return True


def get_prime_pairs_of(number):
    """get prime pairs that make up the sum of (number)"""
    pairs = []

    for i in range(LOWEST_PRIME, number):
        if is_prime(i):
            j = number - i

            if j >= LOWEST_PRIME and is_prime(j):
                if (j, i) in pairs:
                    pass
                else:
                    pairs.append((i, j))
    return pairs


def get_valid_input():
    """validate user input, to be in accordance to parameters of the goldbach conjecture"""
    while True:
        try:
            number = int(input("Enter a number: "))
            if number <= LOWEST_PRIME or number % 2 != 0:
                raise ValueError
            break
        except ValueError:
            print("Error! Please enter whole number >= 4. \n\t(Goldbach's conjecture applies even whole numbers > 2)")

    return number


def main():
  """get_prime_pairs_of method outputs tuples, that we split and print as final output"""
  number = get_valid_input()

  for pair in get_prime_pairs_of(number):
      print(f"The number {number} equals to the sum of {pair[0]} and {pair[1]}")


if __name__ == "__main__":
    main()