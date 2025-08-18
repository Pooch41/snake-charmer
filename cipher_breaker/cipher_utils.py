import json
import math
from collections import Counter


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
NUM_OF_CHAR_IN_ALPHABET = len(ALPHABET)


with open('english_freq.json', 'r') as f:
    ENG_FREQ= json.load(f)


def get_prepared_text(filename: str) -> str:
    """takes in filename, retrieves .txt file with the encoded message, removes everything but lowercase letters"""
    with open(filename, 'r') as f:
        unparsed_text = f.read()

    unparsed_text = unparsed_text.lower()
    parsed_text = ""
    for char in unparsed_text:
        if char.isalpha():
            parsed_text += char

    return parsed_text


def get_text_to_numbers(text: str) -> list:
    """looks if letter is in alphabet const, loops through it returns list of counts(indexes)"""
    return [ALPHABET.find(char) for char in text if char in ALPHABET]


def get_numbers_to_letters(numbers: list[int]) -> str:
    """concats letters to empty return string, by seeking number as count in alphabet string"""
    return ''.join([ALPHABET[num] for num in numbers])


def caesar_shift(numbers: list[int], shift_by: int) -> list[int]:
    """performs caesar shift on numbers - pushes them forward for shift_by"""
    return [(num + shift_by) % NUM_OF_CHAR_IN_ALPHABET for num in numbers]


def get_letter_frequency(text: str) -> dict[str, int]:
    """Gets a dictionary of letter counts for a given string."""
    return Counter(char for char in text.lower() if char in ALPHABET)


def get_chi_squared_score(freq_analysis: list[int]) -> float:
    """uses the chi^2 method to compare bruteforced snippets to a standard freq dict"""
    chi_squared_total = 0
    count_of_observed_occurrences = sum(freq_analysis.values()) #counts total occurrences in substring

    for letter in ALPHABET:
        expected_occurrences = (ENG_FREQ[letter] / 100) * count_of_observed_occurrences

        observed_occurrences = freq_analysis.get(letter, 0)

        if expected_occurrences > 0:
            chi_squared_total += ((observed_occurrences - expected_occurrences) ** 2) / expected_occurrences

    return chi_squared_total


def get_gcd_list(numbers: list[int]) -> int:
    """gets gcd (global common divisor"""
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result
