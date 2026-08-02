def maxDifference(nums):
    min_num = nums[0]
    max_diff = 0

    for num in nums:
        if num < min_num:
            min_num = num

        diff = num - min_num

        if diff > max_diff:
            max_diff = diff

    return max_diff


nums = [7, 1, 5, 3, 6, 4]
print(maxDifference(nums))