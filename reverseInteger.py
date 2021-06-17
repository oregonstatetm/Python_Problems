# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Solution(object):
    def reverse(self, x):
        negative=0
        y=0
        if(x<0):
            negative=1

        if(abs(x)>99):
            for i in range(3):
                y=y+(x%10)
                x=x/10
                y=y*10
        elif(abs(x)>9):        
            for i in range(2):
                y=y+(x%10)
                x=x/10
                y=y*10
        else:
            y=x

        if(y==0 or y<-2147483648 or y>2147483647):
            return 0
    
        if(negative):
            return -y
        else:
            return y