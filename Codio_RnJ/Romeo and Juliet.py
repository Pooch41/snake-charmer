from romeo_and_juliet import PLAY
import re  # going with re-split due to needing multiple deliminators(space, period, question mark, etc.)

roman_numerals = {"II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
                  "X"}  # these aren't words, can't include I(one) because of I(as in me), sets run faster than lists


def get_words(text):
    words = []
    for word in re.split(r'[!-?;:._,\s]+',
                         text):  # re-split works better than default, don't need to fix words w/ punctation.(<<like that one)
        words.append(
            word.lower())  # Optional,logical to count words at the beginning  as the same as in middle. Cat (Cat is orange.) and cat (Orange cat.)
    return words


def word_frequency(words):  # cleaning up as much as feasible
    freq = {}
    for word in words:

        invalid_conditions = [
            word in roman_numerals,  # not english words,
            not word.isalpha(),  # filtering out leftover non-letter characters
            len(word) < 1  # checking for empty list elements, showed up in testing - don't want false positives
        ]
        if any(invalid_conditions):
            continue

        if word in freq:
            freq[word] += 1
        if word not in freq:
            freq[word] = 1
    return freq


def top_n_words(freq, n):
    for _ in range(n):
        word = max(freq, key=freq.get)
        num = freq[word]
        print(f"{word}: {num}")
        freq.pop(word)


def main():
    num_top_words = 50
    text = (PLAY)
    text_dict = word_frequency(get_words(text))
    top_n_words(text_dict, num_top_words)


if __name__ == "__main__":
    main()