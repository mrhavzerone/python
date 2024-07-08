import geometry
import random
import requests


def task_2():
    lenght = random.randint(1, 10)
    width = random.randint(1, 10)

    area = geometry.rectangle_area(lenght, width)
    perimeter = geometry.rectangle_perimeter(lenght, width)

    print(f"Lenght: {lenght}, Width: {width}")
    print(f"Rectangle area: {area}")
    print(f"Rectangle perimeter: {perimeter}")


def task_3():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(f"Post ID: {post['id']}, Title: {post['title']}")
    else:
        print(f"Can`t load data. Status code: {response.status_code}")


task_3()
