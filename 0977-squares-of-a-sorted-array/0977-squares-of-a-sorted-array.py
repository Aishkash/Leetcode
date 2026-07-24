class Solution(object):
    def sortedSquares(self, nums):
        sz=len(nums)
        a=[0]*sz
        left=0
        right=sz-1
        count=sz-1

        while count>=0:
            t=nums[left]*nums[left]
            s=nums[right]*nums[right]
            if t<s:
                a[count]=s
                count-=1
                right-=1
            else:
                a[count]=t
                count-=1
                left+=1
        return a
        
        
        