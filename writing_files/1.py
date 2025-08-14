with open("grades-original.csv", "r") as fileobj:
    data = fileobj.readlines()


with open("grades-bonus.csv", "w") as fileobj:
    for line in data:
        line_bonus = ""
        split_line = line.split(",")
        for item in split_line:
            if split_line.index(item) == 1:
                line_bonus += (str(int(item) + 10) + ",")
            else:
                line_bonus += (item + ",")

        fileobj.write(line_bonus)
