class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        i = 0
        while (i <len(word1) or i < len(word2)):
            if i <len(word1) and i < len(word2): 
                merged = merged + word1[i] + word2[i]
            elif i <len(word1): 
                merged = merged + word1[i]
            elif i <len(word2):
                merged = merged + word2[i]
            i = i+1
        return merged