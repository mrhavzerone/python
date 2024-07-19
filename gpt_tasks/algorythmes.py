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
def buble_sort(numbers):  # didn`t work
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[i]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


print(buble_sort([5, 1, 4, 2, 8]))


# def
