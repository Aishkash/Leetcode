class Solution(object):
    def reverseVowels(self, s):
        vo = set("aeiouAEIOU")
        left=0
        right=len(s)-1
        s = list(s)
        while left<right:
            if s[left] not in vo:
                left += 1
            elif s[right]  not in vo:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)

        