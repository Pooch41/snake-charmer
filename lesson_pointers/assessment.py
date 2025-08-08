
def make_lower(text):
    print(text.lower())

def make_upper(text):
    print(text.upper())

def make_reverse(text):
    print(text[::-1])


text = input("Enter text ending with . or ! or ;")

dispatch = {
    "." : make_upper,
    "!" : make_lower,
    ";" : make_reverse
}

dispatch[text[-1]](text)