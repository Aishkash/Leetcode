class Solution(object):
    def firstUniqChar(self, s):
        sz = len(s)
        a = {}

        for i in s:
            if i not in a:
                a[i] = 0
            a[i] += 1

        k = 0
        while k < sz:
            if a[s[k]] == 1:
                return k
            k += 1

        return -1