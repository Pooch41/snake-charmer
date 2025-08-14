import json

def get_avg(list_of_nums):
    return round((sum(list_of_nums) / len(list_of_nums)), 1)


with open("grades.json", "r") as fileobj:
    data = json.loads(fileobj.read())

write_this = []
for i in data:
    student_name = data[data.index(i)]["name"]
    student_avg = get_avg(data[data.index(i)]["grades"])
    student_max = max(data[data.index(i)]["grades"])
    student_min = min(data[data.index(i)]["grades"])

    print(student_name, student_avg, student_max, student_min)

    student_data = {
        "name": student_name,
        "average grade": student_avg,
        "student max": student_max,
        "student min": student_min
    }

    write_this.append(student_data)

with open("grades_analysis.json", "w") as fileobj:
    fileobj.write(json.dumps(write_this, indent=4))
