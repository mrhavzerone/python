def theory_f():
    some_dict = {
        'name': 'brad',
    }
    name = 'name'
    print(some_dict[name])
    del some_dict[name]
    print(some_dict)
    print(some_dict.get(name, 'user'))


def practice_f():
    my_disk = {}

    # print(id(my_disk))
    # print(type(my_disk))

    my_disk['capacity'] = 480
    my_disk['brand'] = 'Kingston'

    # print(my_disk)
    # print(id(my_disk))

    print(my_disk.popitem())
    print(my_disk)


def task_f():
    empty = {}
    delt = []
    for key in range(0, 6):
        keys = input("enter keys names: ")
        value = key
        empty[keys] = value

    print(empty)


task_f()
