import datetime
MINUTES_IN_HOUR = 60 #const used in get_minutes_in_year_print_current_time
HOURS_IN_DAY = 24
DAYS_IN_YEAR = 365

def get_age_category(age:str ) -> str:
    """take age input, return age category as string"""
    if age < 13:
        return "Child"
    else:
        if age < 20:
            return "Teen"
        else:
            if age < 60:
                return "Adult"
            else:
                return "Senior"


def get_even_numbers(list_of_nums:list) -> list:
    """goes through list, returns list of even numbers"""
    tmp = []
    for x in list_of_nums:
        if x%2==0:
            tmp.append(x)
    return tmp


def get_doubled_numbers(list_of_nums:list) -> list:
    """take input of list, returns list of doubled numbers"""
    result = []
    for item in list_of_nums:
        x = item * 2
        result.append(x)
    return result


def get_max_value(list_of_nums:list) -> int or float:
    """gets list of nums, returns max value(what-ever type num is)"""
    max_val = list_of_nums[0]
    for num in list_of_nums:
      if list_of_nums[num] > max_val:
        max_val = list_of_nums[num]
    return max_val


def get_minutes_in_year_print_current_time(years: int) -> int:
    now = datetime.datetime.now()
    print(now.time())
    minutes_in_year = MINUTES_IN_HOUR * HOURS_IN_DAY * DAYS_IN_YEAR * years
    return minutes_in_year


def get_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if num>= 2:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers


def get_most_frequent_words(fil, n=10):
    """
    Analyze word frequency in a text file.
    Args:
        p (str): Path to the text file
        n (int): Number of top frequent words to return

    Returns:
        list: Top N most frequent words with their counts
    """
    word_frequency_dict = {}
    try:
        f = open(p, 'r')
        t = f.read().lower()
        f.close()
        w = t.split()
        for x in w:
            x = x.strip('.,!?():;[]"\'')
            if x != '':
                if x in word_frequency_dict:
                    word_frequency_dict[x] += 1
                else:
                    word_frequency_dict[x] = 1

        y = list(word_frequency_dict.items())
        for m in range(len(y)):
            for k in range(0, len(y) - m - 1):
                if y[k][1] < y[k + 1][1]:
                    y[k], y[k + 1] = y[k + 1], y[k]
        return y[:n]
    except:
        return "err"