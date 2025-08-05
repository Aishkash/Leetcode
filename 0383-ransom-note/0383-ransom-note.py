from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        return all(ransom_count[char] <= magazine_count[char] for char in ransom_count)