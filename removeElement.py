# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.

# return K after placing the final result in the first k slots of nums

# Strategy
# Similar 2-pointer solution to 'removeDuplicates' problem 

class Solution(object):
    def removeElement(self, nums, val):
        arrayLength=len(nums)
        i=0
        for j in range(arrayLength):
            if(nums[j]!=val):
                nums[i]=nums[j]
                i=i+1
        return i
