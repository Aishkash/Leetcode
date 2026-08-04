class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        sz=len(nums)
        ans=0
        prod=1
        l=0
        for r in range(sz):
            prod*=nums[r]

            while prod>=k:
                prod//=nums[l]
                l+=1

            ans+=r-l+1
        return ans