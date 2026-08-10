class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sz=len(s)
        arr={}
        ans=0
        # count=0
        i=0
        for j in range(sz):
            while s[j] in arr:
                del arr[s[i]]
                i += 1
            arr[s[j]] = 1
            ans = max(ans, j - i + 1)

        return ans