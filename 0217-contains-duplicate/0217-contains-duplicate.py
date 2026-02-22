class Solution(object):
    def containsDuplicate(self, nums):
        a={}
        for num in nums:
            if num not in a:
                a[num]=1
            else:
                a[num]+=1
        for i in nums:
            if a[i]>1:
                return True
        return False