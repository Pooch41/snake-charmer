def number_from_list_of_digits(list_of_digits: list[int]) -> int or None:
    """
    This function gets a list of int digits, like [1, 4, 0]
    And returns the number made out of the digits, as int (140).
    If there is a problem with input values, raises a ValueError.
    If there is a problem with input types, raises a TypeError.
    """

    if list_of_digits is None:
        raise TypeError

    if len(list_of_digits) == 0:
        raise ValueError

    output_str = ""
    for i in range(len(list_of_digits)):
        if list_of_digits[i] < 0:
            raise ValueError
        if type(list_of_digits[i]) != int:
            raise TypeError
        output_str += str(list_of_digits[i])

    return int(f'{output_str:0{len(list_of_digits)}}')

def main():
    pass

if __name__ == '__main__':
    main()
