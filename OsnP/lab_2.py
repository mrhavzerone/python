class Programm():
    user_data = {
        'name': None,
        'age': None,
        'bdate': None
    }

    def hello():
        for keys in Programm.user_data.keys():
            Programm.user_data[keys] = input("Enter your " + keys + ' ')

    def parrot(word, modiifier):
        return word*modiifier

    def swap(a, b):
        return b, a
