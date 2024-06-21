class study_list():
    my_list = []
    my_dict = {'name': 123, 'user': False}

    def append():
        for i in range(0, 10):
            study_list.my_list.append(i)
        print(study_list.my_list)

    def pop():
        for i in range(0, 3):
            study_list.my_list.pop()
        print(study_list.my_list)
        for i in range(0, 3):  # for some reason delete only 0,2,4...
            rm_el = study_list.my_list.pop(i)
            print(study_list.my_list, rm_el)

    def sort():
        study_list.my_list.sort(reverse=True)
        print(study_list.my_list)

    def convert(text):
        study_list.my_list = list(text)

    def convert_dict():
        study_list.my_list = list(study_list.my_dict)

    def min():
        return min(study_list.my_list)

    def max():
        return max(study_list.my_list)

    def sum():
        return sum(study_list.my_list)

    def average():
        return sum(study_list.my_list)/len(study_list.my_list)

    def cut():
        new_list = study_list.my_list[:2]
        print(new_list)
        new_list = study_list.my_list[:-1]
        print(new_list)
        new_list = study_list.my_list[1:-2]
        print(new_list)

    def copy_slice():  # copy slice
        new_list = study_list.my_list[:]
        new_list.append('new')
        print(new_list, '\n', study_list.my_list)
        print(id(new_list) == id(study_list.my_list))

    def copy():
        new_list = study_list.my_list.copy()
        new_list.append('new')
        print(new_list, '\n', study_list.my_list)
        print(id(new_list) == id(study_list.my_list))

    def copy_list():
        new_list = list(study_list.my_list)
        new_list.append('new')
        print(new_list, '\n', study_list.my_list)
        print(id(new_list) == id(study_list.my_list))


study_list.append()
print(len(study_list.my_list))


class Task1:

    def __init__(self, _list):
        self._list = _list

    def main(self):
        print(self._list, len(self._list))
        self._list.pop(2)
        print(self._list, len(self._list))
        self._list.sort(key=lambda x: str(x), reverse=True)
        print(self._list, len(self._list))
        _slist = [True, False]
        self._list.extend(_slist)
        print(self._list, len(self._list))


task_1 = Task1(['zero', 1, 2.5, True, None])
task_1.main()


class Task2:

    def __init__(self, _list, _slist):
        self._list = _list
        self._slist = _slist

    def main(self):

        self._list += self._slist
        print(self._list, self._slist)


task_2 = Task2([1, 3, 5], [0, 2, 4])
task_2.main()

# study_list.append()
# study_list.my_list.clear()
# print(study_list.my_list)

# study_list.append()
# study_list.my_list.extend('abc')
# print(study_list.my_list)

# study_list.copy()
# print(study_list.my_list*2)
# print(study_list.my_list)

# study_list.convert_dict()
# print(study_list.my_list)
# study_list.append()
# study_list.sort()
