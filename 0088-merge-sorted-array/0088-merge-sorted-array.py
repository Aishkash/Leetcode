class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k=m-1
        l=n-1
        sz=m+n-1

        while k>=0 and l>=0:
            if nums1[k]>=nums2[l]:
                nums1[sz]=nums1[k]
                k-=1
            else:
                nums1[sz]=nums2[l]
                l-=1
            sz-=1
        while l>=0:
            nums1[sz]=nums2[l]
            l-=1
            sz-=1

            
        