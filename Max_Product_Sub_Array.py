class Solution:
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            temp = current_max

            current_max = max(
                nums[i],
                current_max * nums[i],
                current_min * nums[i]
            )

            current_min = min(
                nums[i],
                temp * nums[i],
                current_min * nums[i]
            )

            result = max(result, current_max)

        return result

(* 
        Time Complexity
O(n) → We traverse the array only once.
Space Complexity
O(1) → Only a few variables are used. *)
