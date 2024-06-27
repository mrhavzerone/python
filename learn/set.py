# набір - set
# невпорядкована послідовність елементів
# відсутні індекси
# налічує лишу унікальні елементи
# набори можна змінювати
# зберігають однотипні данні в наборах
#
#
# Структура та синтаксис
def example_1():
    some_set = {'one', 'two'}
    other_set = {'two', 'one'}
    print(type(some_set))
    print(some_set == other_set)
    print(len(some_set))
    print(some_set)
# може містити різні елементи, але так ніхто не робить
# не може містити змінювані  об'єкти


def example_2():
    ids = {123, 234, 125, 12, 124}
    ids.remove(123)
    for id in ids:
        print(id)


# Методи наборів
def example_3():
    _set = set()
    print(set)
    _set.add('1920x1080')
    _set.add('800x600')
    s_set = {'1024x768', '800x600'}
    print(_set)
    print(s_set)

    # об'єднання
    # u_set = _set.union(s_set)
    # або
    u_set = _set | s_set
    print('Union: ', u_set)
    del u_set

    # пересічення наборів
    i_set = _set.intersection(s_set)
    print('Intersection', i_set)
    del i_set

    # issubset
    # визначення належності одного набору до іншого
    num = {1, 2, 3, 4}
    other_num = {2, 4}
    print(other_num.issubset(num))
    # issuperset
    # визначення включення одного набору до іншого
    print(num.issuperset(other_num))


def practice_1():
    my_set = {'abc', 'd', 'f', 'y'}
    other_set = {'a', 'f', 'd'}
    print(my_set.intersection(other_set))
    print(my_set.intersection('abcd'))     # &
    # intersection отримує послідовність символів
    print(other_set.issubset(my_set))
    print(my_set.difference(other_set))
    print(my_set.discard('y'))
    print(my_set)

    # example_3()
practice_1()
