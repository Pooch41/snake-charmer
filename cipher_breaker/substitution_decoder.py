import cypher_analysis as ca
NUM_OF_CHAR_IN_ALPHABET = 26


def get_alphabet_number_dict():
    string = ca.file_to_string('alphabet.txt')
    alphabet_list = string.split()
    output_dict = {}
    i = 0

    for letter in alphabet_list:
        output_dict[letter] = i
        i += 1

    return output_dict


def get_numbers_from_cipher(file):
    input_string = ca.file_to_string(file)
    input_string = input_string.lower()

    key_dict = get_alphabet_number_dict()
    words = input_string.split()

    output_list = []

    for word in words:
        sublist = []
        for letter in word:
            if letter in key_dict:
                sublist.append(key_dict[letter])
        sub_tuple = tuple(sublist)
        output_list.append(sub_tuple)

    return output_list


def get_text_to_numbers(text):
    uncoded_numbers = get_alphabet_number_dict()
    split_text = ca.split_string(text)
    output_list = []

    for word in split_text:
        for letter in word:
            uncoded_number = uncoded_numbers[letter]
            output_list.append(uncoded_number)
        output_list.append("")

    return output_list


def get_numbers_to_letters(numbers_list):
    key_dict = get_alphabet_number_dict()
    output_string = ""

    for item in numbers_list:
        for number in item:
            for key in key_dict:
                if number == key_dict[key]:
                    output_string += key
                    pass
        output_string += " "

    output_string = output_string.strip()

    return output_string


def get_shifted_numbers(input_list, shift_by):
    output_list = []
    for item in input_list:
        sublist = []
        for number in item:
            result = number + shift_by
            if result >= NUM_OF_CHAR_IN_ALPHABET:
                result = result % NUM_OF_CHAR_IN_ALPHABET
            sublist.append(result)
        sublist = tuple(sublist)
        output_list.append(sublist)

    return output_list


def bruteforce_decode(cipher_file):
    cipher_num_list = get_numbers_from_cipher(cipher_file)
    for i in range(NUM_OF_CHAR_IN_ALPHABET):
        shifted_numbers = get_shifted_numbers(cipher_num_list, i)
        print(f"Shift Key ({i}) - {get_numbers_to_letters(shifted_numbers)}")


def main():
    bruteforce_decode('cipher.txt')

if __name__ == '__main__':
    main()