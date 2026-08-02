def hasPair(nums, target):
    seen = {}

    for num in nums:
        need = target - num

        if need in seen:
            return True

        seen[num] = True

    return False


nums = [1, 4, 5, 6]
target = 10

print(hasPair(nums, target))