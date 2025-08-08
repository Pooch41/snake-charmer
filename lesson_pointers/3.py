def is_single_word(word):
    return " " not in word

def has_same_start_end_char(word):
    return word[0] == word[-1]

def is_palindrome(word):
    return word == word[::-1]

text = input("Enter a string: ")
choice = input("""  
    'single word' : to check if the text is a single word(no spaces)
    'same char' : to check if the text starts and ends with the same letter
    'palindrome' : to check if the text is palindrome
    
    Enter your choice: """)

func_dict = {
    'single word' : is_single_word,
    'same char' : has_same_start_end_char,
    'palindrome' : is_palindrome,
}

chosen_func = func_dict[choice]
print(chosen_func(text))