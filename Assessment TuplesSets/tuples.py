olymp = ('Rio', 'Brazil', 2016)
x, y, z = olymp

print("-" * 100)

def circle_info(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

circ, area = circle_info(10)
print("area is " + str(area))
print("circumference is " + str(circ))

print("-" * 100)

def date_split_str(date_input):
    split = date_input.split('-')
    return str(split[0]), str(split[1]), str(split[2])

def date_split_int(date_input):
    split = date_input.split('-')
    return int(split[0]), int(split[1]), int(split[2])

date = "24-05-1986"
print(date_split_int(date))

print("-" * 100)