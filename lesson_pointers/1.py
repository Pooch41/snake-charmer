def apply_multiple(text, func_list):
    output = []
    for func in func_list:
        output.append(func(text))
    return output

text = "Hello World"
def first_and_last_char(text: str) -> None:
    print(text[0])
    print(text[-1])

func_list = [first_and_last_char]
apply_multiple(text, func_list)