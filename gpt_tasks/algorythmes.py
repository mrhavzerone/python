# Basic lvl
def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


def is_palindrome(word):
    return word == word[::-1]


def count_elements(lst):
    count = 0
    for element in lst:
        count += 1
    return count

# Middle lvl
