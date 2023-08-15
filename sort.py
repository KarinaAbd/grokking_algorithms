# Sort an array of numbers in three different ways:
# - bubble sorting -> O(n^2)
# - selection sorting -> O(n^2)
# - quick sorting -> O(n log n)

from datetime import datetime
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        finish = datetime.now()
        print(f'{func.__name__}: {finish - start}')
        return result
    return wrapper


@timer
def bubble_sort(numbers: [int]) -> [int]:
    for i in range(len(numbers) -1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]
    return numbers


def find_smallest(numbers: [int]) -> int:
    id_smallest = 0
    for i in range(len(numbers)):
        smallest = numbers[id_smallest]
        if numbers[i] < smallest:
            id_smallest = i
    return id_smallest


@timer
def selection_sort(numbers: [int]) -> [int]:
    sorted_numbers = []
    for _ in range(len(numbers)):
        smallest = find_smallest(numbers)
        sorted_numbers.append(numbers.pop(smallest))
    return sorted_numbers


@timer
def quick_sort(numbers: [int]) -> [int]:
    def inner(numbers):
        if len(numbers) < 2:
            return numbers
        point = numbers[0]
        less = [num for num in numbers[1:] if num < point]
        greater = [num for num in numbers[1:] if num >= point]
        return inner(less) + [point] + inner(greater)
    return inner(numbers)


test_numbers = [1, 2, 5, 2, 3]
assert bubble_sort(test_numbers[:]) == [1, 2, 2, 3, 5]
assert selection_sort(test_numbers[:]) == [1, 2, 2, 3, 5]
assert quick_sort(test_numbers[:]) == [1, 2, 2, 3, 5]
