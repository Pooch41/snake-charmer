def summer(max_value):
    total_sum = 0
    while total_sum < max_value:
        total_sum += int(input("Enter your number: "))
    print(f"Final sum: {total_sum}")


def main():
    max_value = 1000
    summer(max_value)

if __name__ == "__main__":
    main()