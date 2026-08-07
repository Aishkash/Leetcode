class Solution(object):
    def findDuplicate(self, nums):
        a={}
        for i in nums:
            if i in a:
                return i
            a[i]=i
            

        