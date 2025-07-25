def pwd_long_enough(password, req_length):
    return len(password) >= req_length

def pwd_has_symbols(password, allowed_symbols, min_symbols):
    symbol_count = 0
    for char in password:
        if char in allowed_symbols:
            symbol_count += 1
    return symbol_count >= min_symbols

def pwd_has_enough_digits(password, min_digits):
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1
    return digit_count >= min_digits


def main():
    pwd = str(input("Enter Password: "))
    allowed_symbols = ["!", "@", "#", "$", "%"] # From requirements doc
    min_pwd_len = 8 #From requirements doc
    min_symbols = 1 #From requirements doc
    min_digits = 2 #From requirements doc

    if pwd_long_enough(pwd, min_pwd_len) and pwd_has_symbols(pwd, allowed_symbols, min_symbols) and pwd_has_enough_digits(pwd, min_digits):
        print("Password approved!")
    else:
        print("It's not a strong password.")

if __name__ == '__main__':
    main()