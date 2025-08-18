import cipher_utils as util
KASISKI_MIN_SEQ_LENGTH = 3
AVG_LONG_WORD = 7 #reddit said so, seemed reasonable
TOO_LONG_WORD = util.NUM_OF_CHAR_IN_ALPHABET / 2

def get_number_of_repeated_sequences(text) -> dict:
    """looks through text, finds repeated sequences of 3 or longer"""
    all_sequences = {}
    for length in range(KASISKI_MIN_SEQ_LENGTH , AVG_LONG_WORD):
        for i in range(len(text) - length + 1):
            sequence = text[i:i + length]
            if sequence in all_sequences:
                all_sequences[sequence].append(i)
            else:
                all_sequences[sequence] = [i]

    repetitions = {seq: indices for seq, indices in all_sequences.items() if len(indices) > 1}
    return repetitions


def get_distances(repetitions: dict) -> list[int]:
    """looks at indexes, returns distances between repetitions"""
    distances = []
    for indices in repetitions.values():
        for i in range(len(indices) - 1):
            distances.append(indices[i+1] - indices[i])
    return distances


def get_periodic_strings(key_length: int, text: str) -> dict:
    """separates text into periodic strings, based on key length"""
    periodic_strings = {i: "" for i in range(key_length)}
    for i, char in enumerate(text): #enum returns (index, char)
        column_index = i % key_length
        periodic_strings[column_index] += char
    return periodic_strings


def find_best_shift(periodic_string: str) -> int:
    """Finds the best shift for a periodic string using chi-squared analysis."""
    best_shift = 0
    min_score = float('inf')

    for shift in range(util.NUM_OF_CHAR_IN_ALPHABET):

        numbers = util.get_text_to_numbers(periodic_string)
        shifted_numbers = util.caesar_shift(numbers, shift)
        shifted_text = util.get_numbers_to_letters(shifted_numbers)

        # Calculate chi-squared score
        freq_counts = util.get_letter_frequency(shifted_text)
        score = util.get_chi_squared_score(freq_counts)

        # Update if this shift is better
        if score < min_score:
            min_score = score
            best_shift = shift

    return best_shift

def reassemble_text(periodic_strings: dict) -> str:
    """Reassembles the periodic strings into a single message."""
    key_length = len(periodic_strings)
    max_len = max(len(s) for s in periodic_strings.values())
    output = []

    for i in range(max_len):
        for j in range(key_length):
            if i < len(periodic_strings[j]):
                output.append(periodic_strings[j][i])

    return "".join(output)

def decrypt_with_known_key(text: str, key: str) -> str:
    """Decrypts text using known key"""
    known_numbers = util.get_text_to_numbers(text)
    key_to_numbers = util.get_text_to_numbers(key)
    shifted_by_key_numbers = []
    i = 0
    for number in known_numbers:
        temp_number= number - key_to_numbers[i]
        if temp_number > 25:
            temp_number = temp_number % util.NUM_OF_CHAR_IN_ALPHABET

        i += 1
        if i == len(key_to_numbers):
            i = 0

        shifted_by_key_numbers.append(temp_number)

    decoded_text = util.get_numbers_to_letters(shifted_by_key_numbers)
    return decoded_text

def main():
    ciphertext = util.get_prepared_text("message.txt")

    repetitions = get_number_of_repeated_sequences(ciphertext)
    distances = get_distances(repetitions)
    key_length = util.get_gcd_list(distances)


    print(f"GCD: {key_length}") # overlong words unlikely?
    if key_length > TOO_LONG_WORD:
        print(f"GCD longer than {TOO_LONG_WORD} is too long.")
        key_length = int(key_length / 2)
        print(f"GCD: {key_length}")

    periodic_strings = get_periodic_strings(key_length, ciphertext)

    key_shifts = {} # use bruteforced string snippets with chi^2 to find most likely shifts
    for i in range(key_length):
        key_shifts[i] = find_best_shift(periodic_strings[i])

    print(f"Key shifts: {key_shifts}")
    key_list = []
    for key in key_shifts:
        key_list.append(key_shifts[key])
    print(util.get_numbers_to_letters(key_list))
    inverse_key_shifts = {}
    inverted_list = []
    for key in key_shifts:
        inverted_key = util.NUM_OF_CHAR_IN_ALPHABET - key_shifts[key]
        inverse_key_shifts[key] = inverted_key
        inverted_list.append(inverse_key_shifts[key])
    print("Inverse key shift:", inverse_key_shifts)
    inverted_password = util.get_numbers_to_letters(inverted_list)
    print(inverted_password)

    decrypted_strings = {}
    for i, p_string in periodic_strings.items(): # i == key_id, p_string == lowest chi^2 score string
        numbers = util.get_text_to_numbers(p_string)
        decrypted_numbers = util.caesar_shift(numbers, key_shifts[i])
        decrypted_strings[i] = util.get_numbers_to_letters(decrypted_numbers)

    final_plaintext = reassemble_text(decrypted_strings)
    print("Message 1: ", final_plaintext)

    ciphertext2 = util.get_prepared_text("message_2.txt")
    message2 = decrypt_with_known_key(ciphertext2, inverted_password)
    print("Message 2: ", message2)


if __name__ == '__main__':
    main()