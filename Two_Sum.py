class Solutions:
    def twosum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in seen:
                return [seen[need], i]

            seen[nums[i]] = i


nums = [2, 7, 9, 11, 15]
target = 9

obj = Solutions()
print(obj.twosum(nums, target))