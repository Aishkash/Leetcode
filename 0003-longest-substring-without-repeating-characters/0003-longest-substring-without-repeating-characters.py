class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        left = 0
        max_length = 0

        for i in range(len(s)):
            if s[i] in char_index and char_index[s[i]] >= left:
                left = char_index[s[i]] + 1
            char_index[s[i]] = i
            max_length = max(max_length, i - left + 1)
        
        return max_length