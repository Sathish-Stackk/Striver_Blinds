class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        xor = n

        for i in range(n):
            xor ^= i
            xor ^= nums[i]

        return xor

#   Complexity ::
# Time  : O(n)
# Space : O(1)
