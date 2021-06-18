# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#Need to handle up to the limit.
class Solution(object):
    def reverse(self, x):
        negative=0
        y=0
        i=1
        # Set Negative Flag
        if(x<0):
            negative=1
        x=abs(x)
        
        while((10**i)<x):
            i=i+1
        
        if(10**i==x):
            if(negative):
                return -1
            else:
                return 1

            
        for j in range(i):
            y=y+(x%10)
            x=x/10
            y=y*10
        
        y=y/10

        if(y==0 or y<-2147483648 or y>2147483647):
            return 0
    
        if(negative):
            return -y
        else:
            return y