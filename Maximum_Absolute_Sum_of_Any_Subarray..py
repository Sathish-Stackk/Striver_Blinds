class Solution:
    def maxAbsoluteSum(self, nums):
        max_sum = 0
        min_sum = 0
        answer = 0

        for num in nums:
            max_sum = max(num, max_sum + num)
            min_sum = min(num, min_sum + num)

            answer = max(answer, abs(max_sum), abs(min_sum))

        return answer


# Time Complexity
# O(n)
# Space Complexity
# O(1)
