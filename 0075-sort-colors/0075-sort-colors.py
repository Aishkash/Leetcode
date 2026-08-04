class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a=0
        b=len(nums)-1
        i=0
        while i<=b:
            if nums[i]==0:
                nums[i],nums[a]=nums[a],nums[i]
                a+=1
                i+=1
            elif nums[i]==2:
                nums[i],nums[b]=nums[b],nums[i]
                b-=1
            else:
                i+=1
                