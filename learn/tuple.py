def example_1():  # Доступ та принцип роботи з кортежем
    my_tuple = ('apple', 'banana', 'lime')
    print(type(my_tuple))
    users = (
        {
            'id': 1,
            'name': 'user'
        },
        {
            'id': 2,
            'name': 'root'
        }
    )
    print(users[0]['name'])

    users[0]['name'] = 'kali'

    print(users[0]['name'])


def example_2():  # Формування кортежу зі змінних
    num_1, num_2, num_3 = '1', '2', '3'
    num_tupple = (num_1, num_2, num_3)
    print(num_tupple)


def example_3():  # додавання кортежей
    external_ids = (312, 412)
    internal_ids = (123, 524, 213)
    all_ids = external_ids+internal_ids
    print(all_ids)


def example_4():  # методи  index та count
    internal_ids = (123, 524, 213, 123, 123)
    print(internal_ids.count(123))
    print(internal_ids.index(123, 0+1))
    # можна передавати декілька аргументів,
    # другий аргумент методу index позничає
    # звідки буде починатись пошук наступного елементу


def example_5():  # варіант зміни кортежу
    internal_ids = (123, 524, 213)
    internal_ids_list = list(internal_ids)
    internal_ids_list.append(432)
    internal_ids = tuple(internal_ids_list)
    print(internal_ids)


example_4()
