# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity

# Strategy
# Implement Binary Search

class Solution(object):
    def searchInsert(self, nums, target):
        arrayLength=len(nums)
        midpoint=arrayLength/2
        print("Length",arrayLength)
        print("Midpoint",midpoint)
        print("Target",target)
        print("MidValue",nums[midpoint])
        print(nums)

        for i in range(arrayLength):
            print(i,"Mid:",midpoint)
            if(nums[midpoint]==target):
                return midpoint # Target found
            elif((nums[midpoint]<target) and (nums[midpoint+1]>target)):
                return midpoint+1 # Target not in array, expected location found
            elif((nums[midpoint]<target) and midpoint+1==arrayLength):
                return midpoint+1 # Target not in array
            elif((nums[midpoint]>target) and midpoint==0):
                return 0
            elif(nums[midpoint]>target):
                midpoint=midpoint/2
            else:
                temp=(arrayLength-midpoint)/2+midpoint
