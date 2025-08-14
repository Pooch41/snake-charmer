import json

def get_avg(list_of_nums):
    return round((sum(list_of_nums) / len(list_of_nums)), 1)


with open("cars.json", "r") as fileobj:
    data = json.loads(fileobj.read())

car_avg_price = []
car_year = []

for car in data["cars"]:
    car_avg_price.append(car["price"])
    car_year.append(car["year"])


car_info = {
   "avg_price": get_avg(car_avg_price),
   "min_year": min(car_year),
   "max_year": max(car_year)
}


with open("car_analysis.json", "w") as fileobj:
    fileobj.write(json.dumps(car_info, indent=4))