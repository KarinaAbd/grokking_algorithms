# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

def binary_search(numbers: [int], target: int) -> int:
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = numbers[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


test_numbers = [-1, 0, 3, 5, 9, 12]
assert binary_search(test_numbers, 9) == 4
assert binary_search(test_numbers, -1) == 0
assert binary_search(test_numbers, 4) == -1
