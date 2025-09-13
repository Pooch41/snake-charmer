import requests

def get_name_color_response():
    while True:
        user_name = input("Please enter your name: ")
        if len(user_name) > 1:
            break

    while True:
        user_color = input("Please enter your favourite color: ")
        if len(user_color) > 1:
            break

    request = requests.get('https://learningserver.masterschool.com/http-basics/get-me',
                           params = {'name': user_name, 'color': user_color})

    return request

def post_name_password_response():
    while True:
        user_name = input("Please enter your name: ")
        if len(user_name) > 1:
            break

    while True:
        user_password = input("Please enter your password: ")
        if len(user_password) > 1:
            break

    request = requests.post('https://learningserver.masterschool.com/http-basics/post-me',
                           data = {'username': user_name, 'password': user_password})

    return request

print(post_name_password_response().text)
