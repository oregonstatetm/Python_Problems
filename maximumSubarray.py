# Maximum Subarray
#
# Problem Description: 
# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSub=nums[0]
        maxSub=nums[0]
        arrayLength=len(nums)
        for i in range(1,arrayLength):
            if(currentSub<0):               # Discard any subarray that becomes negative
                currentSub=0
            currentSub+=nums[i]
            if(maxSub<currentSub):          # Test for new maximum after each iteration
                maxSub=currentSub
        
        return maxSub