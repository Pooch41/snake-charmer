from math import sqrt


def is_divisible_by(number, by):


    return number % by == 0


def is_prime(number):


    if number < 2: # 0 1 are not primes
        return False

    for i in range(2, (int(sqrt(number)) + 1)): # if divisor found on sqrt of num == applies to num == fewer checks
        if is_divisible_by(number, i): #if any is found, number is composite
            return False
         # indent on level of for loop to round out search

    return True


def primes_in_range(start, end):


    for i in range(start, end):
        if is_prime(i):
            print(f"The number {i} is prime")


def main():

    primes_in_range(int(input("Enter start range: ")), int(input("Enter end range: ")))


if __name__ == '__main__':
    main()