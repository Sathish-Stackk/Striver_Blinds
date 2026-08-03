class Solution:
    def firstduplicate(self,nums):
        seen =set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)
        return -1

nums = [2,5,1,2,3,5,1]
obj=Solution()
print(obj.firstduplicate(nums))



# Time Complexity:

# Set lookup: O(1) on average.
# Set insertion: O(1) on average.

# Space Complexity:

# Space: O(n)