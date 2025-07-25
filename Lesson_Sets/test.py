def parse_log(input_text):
    text_output = []

    for line in input_text:
        temp_holder = line.split(" | ")
        temp_holder = [item.strip() for item in temp_holder]
        text_output.append(tuple(temp_holder))

    assert len(text_output) > 0, "Empty log — check upstream download."
    return text_output


def get_visitors(input_text):
    text_output = []

    for item in input_text:
        text_output.append((item[1]))

    return text_output


def unique_visitors(visitor_input):
    return set(visitor_input)


def daily_totals(parsed_input):
    assert len(parsed_input) > 0, "Empty input log — check upstream download."

    output_dict = {}
    temp_holder = []

    for item in parsed_input:
        date = item[0].split()[0]
        temp_holder.append(date)

    for item in temp_holder:
        if item not in output_dict:
            output_dict[item] = 1
        else:
            output_dict[item] += 1

    return output_dict


rows = [
    "2024-07-23 14:00:02 | v123 | /guild-board",
    "2024-07-23 14:10:20 | v888 | /shop",
    "2024-07-23 14:15:47 | v123 | /quests"
]


def main():
    split_inputs = parse_log(rows)
    visitors = get_visitors(split_inputs)

    print(f"Total visitors: {len(visitors)}")
    print(f"Unique visitors: {len(unique_visitors(visitors))}")
    print(f"Busiest Day: {max(daily_totals(split_inputs))}")


if __name__ == "__main__":
    main()