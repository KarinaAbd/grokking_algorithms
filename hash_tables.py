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
