class Solution:
    def containDuplicate(self,nums):
        seen =set()
        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        return False
nums=[1,32,5,6,43,3]
obj=Solution()
print(obj.containDuplicate(nums))



# Time Complexity:

# O(n)

# Space Complexity

# Space = O(n)