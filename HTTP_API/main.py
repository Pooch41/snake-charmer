import requests

task3_1 = requests.request(url="https://jsonplaceholder.typicode.com/posts/98",
                           method="GET")

if task3_1.ok:
    task3_1_dict = task3_1.json()
    print("TASK 3.1:")
    for key in task3_1_dict:
        print(key + ':', task3_1_dict[key])
    print("-" * 100)

    print("TASK 3.2:\nNumber of attributes:", len(task3_1_dict))
    print("-" * 100)

task3_3 = requests.request(url="https://jsonplaceholder.typicode.com/posts/21/comments",
                           method="GET")
if task3_3.ok:
    task3_3_list = task3_3.json()
    print("TASK 3.3:")
    print("Number of comments:",len(task3_3_list))

task4_1 = requests.request(url="https://jsonplaceholder.typicode.com/posts/",
                           method="POST",
                           data = {
                               'title': "smashmouth",
                               'body': "somebody once told me",
                               'userId': 420
                           })

print("-" * 100)
if task4_1.ok:
    print("TASK 4.1:")
    print(task4_1.json())

task5_1 = requests.request(url="https://jsonplaceholder.typicode.com/posts/28",
                           method="PUT",
                           data = {
                               'body': "updated body",
                           })

print("-" * 100)
if task5_1.ok:
    print("TASK 5.1:")
    print(task5_1.json())

task6_1 = requests.request(url="https://jsonplaceholder.typicode.com/posts/60",
                           method="DELETE"
                            )
print("-" * 100)
if task6_1.ok:
    print("TASK 6.1")
    print(task6_1.json())