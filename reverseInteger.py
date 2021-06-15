# Given a signed 32-bit integer x, return x with its digits reversed. 
# rIf reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Solution(object):
    def reverse(self, x):
        y=x%10
        x=x/10
        y=y*10
        y=y+(x%10)
        x=x/10
        y=y*10
        y=y+(x%10)
        x=x/10
        return y