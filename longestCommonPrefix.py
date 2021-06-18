Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):    
        for i in range(len(strs)):
            print(strs[i])
            print(strs[i][0])