def capitalize_words(sentence):
    """Capitalize the first letter of each word in the sentence"""
    words = sentence.split()
    capitalised_words = []
    for word in words:
        word = word.capitalize()
        capitalised_words.append(word)
    return " ".join(capitalised_words)

def main():
    sentence = "hello world, this is a test."
    capitalized_sentence = capitalize_words(sentence)
    print(capitalized_sentence)
    # Expected output: "Hello World, This Is A Test."

if __name__ == "__main__":
    main()
