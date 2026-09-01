class Solution(object):
    def peakIndexInMountainArray(self, arr):
        sz=len(arr)
        ans=0
        left,right=0,sz-1
        while left<right:
            mid=(left+right)//2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
