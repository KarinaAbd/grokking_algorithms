# 1 Next Greater Element I

# The next greater element of some element x in an array is the first greater element that is to the right of x
# in the same array. You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and
# determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


def nextGreaterElement(nums1: [int], nums2: [int]) -> [int]:
    result = []
    mapping = {num: index for index, num in enumerate(nums2)}
    l = len(nums2)

    for num in nums1:
        next_index = mapping[num] + 1
        res = -1
        if next_index < l:
            for number in nums2[next_index:]:
                if number > num:
                    res = number
                    break
        result.append(res)
    return result


assert nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
assert nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
assert nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]) == [7, 7, 7, 7, 7]

# 2 N-Repeated Element in Size 2N Array
# You are given an integer array nums with the following properties:
# - nums.length == 2 * n.
# - nums contains n + 1 unique elements.
# - Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

from collections import Counter


def repeatedNTimes(nums: [int]) -> int:
    c = Counter(nums)
    res = c.most_common(1)
    return res[0][0]


assert repeatedNTimes([1, 2, 3, 3]) == 3
assert repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2
assert repeatedNTimes([5,1,5,2,5,3,5,4]) == 5
