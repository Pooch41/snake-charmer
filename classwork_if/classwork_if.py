def print_break_line() -> None:
    print("-" * 100)


def get_total_gold_weight(sack_list: list[float]) -> float:
    """gets total weight of gold sacks, return total weight of gold"""
    total_gold_weight = 0
    for sack in sack_list:
        total_gold_weight += sack
    return total_gold_weight


CARRIABLE_SACK = 5


def get_carriable_sack_weight(sack_list: list[float]) -> float:
    """gets total of sacks that weight 5 or below, return total weight of those"""
    carriable_sack_weight = 0
    for sack in sack_list:
        if sack <= CARRIABLE_SACK:
            carriable_sack_weight += sack
    return carriable_sack_weight


sacks = [2.33, 4.1, 8.5, 6.66, 2.4]
print(f"Total sack weight: {get_total_gold_weight(sacks)}")
print(f"Carriable sack weight: {get_carriable_sack_weight(sacks)}")
print_break_line()

UNLUCKY_NUMBER = 13


def get_unlucky_necklace_count(necklace_list: list[int]) -> int:
    """count all necklaces with 13 pearls, return that count"""
    unlucky_necklace_count = 0
    for necklace in necklace_list:
        if necklace == UNLUCKY_NUMBER:
            unlucky_necklace_count += 1
    return unlucky_necklace_count


necklaces = [12, 13, 22, 18, 13, 10, 30, 15, 13, 12]
print(f"Unlucky necklaces: {get_unlucky_necklace_count(necklaces)}")
print_break_line()

SHORT_NAME_LEN = 4


def get_common_name_counts(name_list: list[str]) -> tuple[int, int]:
    """gets names starting with H and those starting with L + Four letters long, returns results in tuple"""
    names_starting_h = 0
    names_starting_l_len_four = 0
    for name in name_list:
        if name[0].lower() == "h":
            names_starting_h += 1
        elif name[0].lower() == "l" and len(name) == SHORT_NAME_LEN:
            names_starting_l_len_four += 1
    return names_starting_h, names_starting_l_len_four


names = ["Emma", "Felix", "Henry", "Linn", "Lina", "Felix", "Hannah", "Noah", "Marie", "Leon"]
names_starting_h, names_starting_l_len_four = get_common_name_counts(names)
print(f"Names starting with H: {names_starting_h}")
print(f"Names starting with L, that are four letters long: {names_starting_l_len_four}")
print_break_line()


def get_total_box_count(box_list: list[int]) -> int:
    """gets total box count, box in previous box, returns total count"""
    total_box_product = 1 # we start with 1 because the world is a box
    total_count = 0
    for box in box_list:
        total_box_product *= box
        total_count += total_box_product
    return total_count


boxes = [8, 4, 6]
print(f"Total box count: {get_total_box_count(boxes)}")
print_break_line()


def get_class_average(grade_list: list[float]) -> float:
    """calulcates and returns class average grade"""
    total = 0
    for grade in grade_list:
        total += grade
    return total / len(grade_list)


grades = [1.0, 2.1, 1.5, 3.0, 1.0, 1.2, 3.5, 1.0]
print(f"Class average: {get_class_average(grades):.2f}")
print_break_line()


def get_fastest_run(run_time_list: list[float]) -> float:
    """finds and returns fastest run time"""
    fastest_run_time = run_time_list[0]
    for run_time in run_time_list:
        if fastest_run_time > run_time:
            fastest_run_time = run_time
    return fastest_run_time


times = [31.3, 29.8, 29.4, 30.3, 28.9, 29.4]
print(f"Fastest run time: {get_fastest_run(times)}")
print_break_line()
