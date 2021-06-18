Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):
        if(x<0): #Negative numbers are not palendromes
            return False
        if(x<10 and x>0): # Single digit is a palendrome
            return True
        if(x==10): # Handle special case for integer reverse code
            return False
        if(x>2147483647): #Invalid - to large
            return False
        i=1
        y=0
        temp=x
        #Count Number of Digits
        while((10**i)<x):
            i=i+1
        #Reverse x
        for j in range(i):
            y=y+(x%10)
            x=x/10
            y=y*10
        
        y=y/10
        print("Y:",y)
        print("X:",temp)
        
        if(y==temp):
            return True
        else:
            return False

    
        