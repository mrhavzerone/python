import random
import math


class Programm():
    # my own solution
    def max_abc(a, b, c):
        if max(a, b) <= c:
            return c, max(a, b), min(a, b)
        elif min(a, b) <= c:
            return max(a, b), c, min(a, b)
        else:
            return max(a, b), min(a, b), c
    # i love python, finded solution

    def max_abcd(a, b, c, d):
        values = [a, b, c, d]
        values.sort(reverse=True)
        return tuple(values)

    def hit():
        x0 = random.randint(0, 50)
        y0 = random.randint(0, 50)
        r = random.randint(5, 25)
        x = float(input("enter value x: "))
        y = float(input("enter value y: "))
        if math.sqrt((x - x0)**2 + (y - y0)**2) < r:
            print(
                f"dot({x}, {y}) have a hit in circle({x0}, {y0}) with radius({r})")
        else:
            print(
                f"dot({x}, {y}) miss a hit in circle({x0}, {y0}) with radius({r})")


Programm.hit()
# print("max value:",
#       Programm.max_abcd(
#           int(
#               input("enter value a: ")
#           ),
#           int(
#               input("enter value b: ")
#           ),
#           int(
#               input("enter value c: ")
#           ),
#           int(
#               input("enter value d: ")
#           )
#       )
#       )
