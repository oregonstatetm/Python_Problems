#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

class Solution(object):
    def characterMatch(self,strs,prefixPosition,numberStrings,currentLetter):
        for j in range(1,numberStrings): #Skip First String
            if(currentLetter==strs[j][prefixPosition]):
                print("TestString: ", strs[j][prefixPosition])
                print("Match")
            else:
                print("NoMatch")
                return 0 # No Match
        return 1

    def longestCommonPrefix(self, strs):
        numberStrings = len(strs)  
        substring=[]
        teststring=[]
        minLength=200
        firstWord = list(strs[0])
        currentLetter = firstWord[0]
        firstLength = len(strs[0])
        matchCount=0
        for i in range(firstLength): #6
            print("MatchString: ", currentLetter)
            characterReturn = self.characterMatch(strs,i,numberStrings,currentLetter)
            matchCount=matchCount+characterReturn
            if(characterReturn==1):
                currentLetter = firstWord[i+1]
            else:
                break # No Match
        result=""
        if(matchCount==0):
            return ""
        for k in range(matchCount):
            result=result+firstWord[k].encode('UTF8')      
        return result