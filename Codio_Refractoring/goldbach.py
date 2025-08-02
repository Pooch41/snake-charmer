LOWEST_PRIME = 2

def get_prime_pairs_of(number):
    """get prime pairs that make up the sum of (number)"""
    pairs = []

    for i in range(LOWEST_PRIME, number):
        i_is_prime = True
        x = LOWEST_PRIME

        while x < i:
            if i % x == 0:
                i_is_prime = False
            x += 1

        if i_is_prime:
            j = number - i

            if j >= LOWEST_PRIME:
                j_is_prime = True
                x = LOWEST_PRIME

                while x < j:
                    if j % x == 0:
                        j_is_prime = False
                    x += 1

                if j_is_prime:
                    if (j, i) in pairs:
                        pass
                    else:
                        pairs.append((i, j))

    return pairs

while True:
    try:
        number = int(input("Enter a number: "))
        if number <= LOWEST_PRIME or number % 2 != 0:
            raise ValueError
        break
    except ValueError:
        print(
            "Error! Please enter whole number >= 4. \nGoldbach's conjecture only applies even whole numbers greater than 2")

for pair in get_prime_pairs_of(number):
    print(f"The number {number} equals to the sum of {pair[0]} and {pair[1]}")
