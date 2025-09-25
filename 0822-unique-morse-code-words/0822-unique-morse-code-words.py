class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()
        
        for word in words:
            current_transformation = ""
            for char in word:
                # Get the index of the character (e.g., 'a' is 0, 'b' is 1)
                index = ord(char) - ord('a')
                current_transformation += morse_code[index]
            
            # Add the completed transformation to the set
            transformations.add(current_transformation)
            
        return len(transformations)


