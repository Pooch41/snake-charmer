def has_full_stop(text: str) -> bool:
    """checks if text has a full stop character (.)"""
    for char in text:
        if char == ".":
            return True
    return False

def is_only_dollar_signs(text:str) -> bool:
    """validates that text is ONLY dollar signs ($)"""
    for char in text:
        if char != "$":
            return False
    return True


def are_between_10_and_20(lst_of_nums: list[float]) -> bool:
    """checks if every member of list is between 10 and 20"""
    for number in lst_of_nums:
        if number < 10 or number > 20:
            return False
    return True