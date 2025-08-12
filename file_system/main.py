with open("SP500.txt", "r") as txt_file:
    lines = txt_file.readlines()[1:]

record = False
start_date = "6/1/2016"
end_date = "5/1/2017"
sp = []
interest = []
for line in lines:
    split_line = line.split(",")
    if split_line[0] == start_date:
        record = True
    if split_line[0] == end_date:
        record = False
    if record:
        sp.append(float(split_line[1]))
        interest.append(float(split_line[5]))

print(sp)
print(interest)

print(sum(sp)/len(sp))
print(max(interest))
mean_SP = round(sum(sp)/len(sp), 1)
max_interest = max(interest)