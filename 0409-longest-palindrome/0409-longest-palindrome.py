class Solution(object):
    def longestPalindrome(self, s):
        sz=len(s)
        if sz==1:
            return 1
        a={}
        for i in s:
            if i not in a:
                a[i]=0
            a[i]+=1
        ans=0
        odd=False
        count=0
        for k in a:
            if a[k]%2==0:
                count+=a[k]
            else:
                count+=a[k]-1
                odd=True
        if odd:
            count+=1
        return count
        