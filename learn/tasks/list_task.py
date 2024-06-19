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
