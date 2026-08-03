class Solution:
    def maxSubArray(self,nums):

        currentSum=nums[0]
        maxSum=nums[0]

        for i in range(1,len(nums)):
            currentSum=max(nums[i],currentSum+nums[i])

            maxSum=max(maxSum,currentSum)

        return maxSum

nums = [5,4,-1,7,8]
obj=Solution()
print(obj.maxSubArray(nums))