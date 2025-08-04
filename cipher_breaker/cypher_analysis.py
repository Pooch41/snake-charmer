import re

def file_to_string(filename):
    with open(filename, 'r') as f:
        file_contents = f.read()

    return file_contents
def split_string(string):
    input_string = string.lower()
    s = re.split(r'[;,.\s]+', input_string)
    return s


def get_letter_frequency(string):
    freq_dict = {}
    coded_list = split_string(string)

    for word in coded_list:
        for letter in word:
            if letter in freq_dict:
                freq_dict[letter] += 1
            else:
                freq_dict[letter] = 1

    return freq_dict

def get_ranked_frequency(string):
    freq_dict = get_letter_frequency(string)
    freq_dict_copy = freq_dict.copy()
    ranked_dict = {}
    for letter in freq_dict:
        x = max(freq_dict_copy, key=freq_dict_copy.get)
        if not x.isalpha():
            del freq_dict_copy[x]
        else:
            ranked_dict[x] = freq_dict_copy[x]
            del freq_dict_copy[x]

    return ranked_dict

def get_frequency_analysis(string):

    sorted_dict = get_ranked_frequency(string)
    print(sorted_dict)
    print(f"Length of dict - {len(sorted_dict)}")

def main():
    pass

if __name__ == '__main__':
    main()