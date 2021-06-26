# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

# Essentially, Once an element is encountered, you simply need to bypass its duplicates and move on to the next unique element.

# Return k after placing the final result in the first k slots of nums.
 
class Solution(object):
    def removeDuplicates(self, nums):
        i=0 # pointer to unique element
        length=len(nums)
        if length==0:
            return 0
        for j in range(1, length):
            if(nums[j]!=nums[i]):
                i=i+1
                nums[i]=nums[j]
        return i+1