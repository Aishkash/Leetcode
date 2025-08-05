from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for letters in ransom_count:
            if ransom_count[letters]>magazine_count[letters]:
                return False
        return True        