class Solution(object):
    def characterReplacement(self, s, k):
        sz = len(s)
        i = 0
        j = 0
        count = {}
        ans = 0

        while j < sz:
            count[s[j]] = count.get(s[j], 0) + 1

            mx = max(count.values())

            if (j - i + 1) - mx <= k:
                ans = max(ans, j - i + 1)
                j += 1
            else:
                count[s[i]] -= 1
                i += 1
                j += 1

        return ans