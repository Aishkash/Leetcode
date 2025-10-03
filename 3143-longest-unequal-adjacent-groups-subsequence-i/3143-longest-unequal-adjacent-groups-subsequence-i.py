class Solution(object):
    def getLongestSubsequence(self, words, groups):
        arr = [0]  # start with first index
        for i in range(1, len(groups)):
            if groups[i] != groups[arr[-1]]:
                arr.append(i)
        j=[]
        for i in arr:
            j.append(words[i])
        return j    
