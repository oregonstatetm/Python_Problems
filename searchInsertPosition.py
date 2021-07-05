# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity

# Strategy
# Implement Binary Search

class Solution(object):
    def searchInsert(self, nums, target):
        arrayLength=len(nums)
        midpoint=arrayLength/2

        for i in range(arrayLength):
            print(i,"Mid:",midpoint)
            if(nums[midpoint]==target): # Target found
                return midpoint 
            elif((nums[midpoint]<target) and midpoint+1==arrayLength): # Target out of range - high
                return midpoint+1 
            elif((nums[midpoint]>target) and midpoint==0): # Target out of range - low
                return 0
            elif((nums[midpoint]<target) and (nums[midpoint+1]>target)): # Target not in array, expected location found
                return midpoint+1
            elif(nums[midpoint]>target):
                midpoint=midpoint/2
            elif(nums[midpoint]<target):
                temp=(arrayLength-midpoint)/2
                midpoint=temp+midpoint

