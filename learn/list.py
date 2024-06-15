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
# study_list.copy()
# print(study_list.my_list*2)
# print(study_list.my_list)
# study_list.convert_dict()
# print(study_list.my_list)
# study_list.append()
# study_list.sort()
