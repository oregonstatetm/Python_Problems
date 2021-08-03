# Length of Last Word
#
# Description: Given a string s consists of some words separated by spaces.
# Return the length of the last word in the string. 
# If the last word does not exist, return 0.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        removeTrailingSpaceString=s.rstrip()        # Handle trailing space case. example: "a "
        lengthWord=len(removeTrailingSpaceString)
        count=0
        for i in reversed(range(lengthWord)):
            count+=1
            if(removeTrailingSpaceString[i]==" "):  # Found last word length
                return count-1
        return count                                # Handle no-space case. example: "bat"
        