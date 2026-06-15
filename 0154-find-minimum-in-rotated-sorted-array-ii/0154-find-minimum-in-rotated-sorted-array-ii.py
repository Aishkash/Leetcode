class Solution(object):
    def findMin(self, nums):
        a=len(nums)
        l=0
        r=a-1 
        while l<=r:
            mid=(l+r)//2
            print(mid,l,r)
            # if l==r==mid:
            #     return nums[l]
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[l]:
                r=mid
            else:
                r-=1
            
            # elif nums[l]==nums[mid] and nums[mid]==nums[r]:
            #     l+=1
            #     r-=1
            
        return nums[l]