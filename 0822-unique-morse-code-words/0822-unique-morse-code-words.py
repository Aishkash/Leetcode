class Solution(object):
    def uniqueMorseRepresentations(self, words):
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        answer=set()

        for i in words:
            a=""
            for j in i:
                index=ord(j)-ord('a')
                a+=code[index]
            answer.add(a)

        return  len(answer)     