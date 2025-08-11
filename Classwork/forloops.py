def name_printer(list_of_names):
    """takes list, if names match villains, shoos away, otherwise welcomes"""
    for name in list_of_names:
        if name == "Vecna" or name == "Acererak":
            print(f"{name}! Begone, lich.")
        else:
            print(f"{name}! Welcome.")


def get_vowel_count(string):
    """counts vowels in a string, returns total"""
    vowels = 0
    for char in string.lower():
        if char in "aeiou":
            vowels += 1

    return vowels


def check_grades(list_of_grades):
    """checks if grade pass - print out answer."""
    for grade in list_of_grades:
        if grade > 70:
            print(f"{grade} passes.")
        else:
            print(f"{grade} fails.")


def get_processed_numbers(list_of_numbers):
    """ > 100 breaks, skip negatives, return total"""
    total = 0
    for number in list_of_numbers:
        if number < 0:
            continue
        if number > 100:
            break
        else:
            total += number

    return total


def filter_complex_words(list_of_words):
    """count words w/ len > 5, break if len > 10"""
    eligible_word_count = 0
    for word in list_of_words:
        if len(word) > 10:
            break
        elif len(word) > 5:
            eligible_word_count += 1

    return eligible_word_count


names = ["Aveena", "Harold", "Vecna", "Boborillius", "Chen", "Rexxar", "Acererak"]
name_printer(names)

print("-" * 100)

string_to_process = "The quick brown fox jumps over the lazy dog"
print(get_vowel_count(string_to_process)) #expected 11

print("-" * 100)

grades = [99, 1, 10, 30, 71, 69, 100]
print(check_grades(grades)) #91/71/100 pass rest fail

print("-" * 100)

numbers = [1, 10, -30, 66, 101, 9]
print(get_processed_numbers(numbers)) #expected 77

print("-" * 100)

words = ["Apples", "Joel", "Hydroelectric"]
print(filter_complex_words(words)) #expected 1

print("-" * 100)