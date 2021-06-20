#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        numberStrings = len(strs)  
        substring=[]
        teststring=[]
        minLength=10000  
        # Calculate the shortest string
        for i in range(numberStrings):
            if(len(strs[i])<minLength):
                minLength=len(strs[i])
            print(strs[i])
        
        print(minLength)
