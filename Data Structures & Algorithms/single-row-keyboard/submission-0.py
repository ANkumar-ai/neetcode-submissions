class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        ctr=0

        hashmap={}

        for i in range(len(keyboard)):

            hashmap[keyboard[i]]=i

        prev=0


        for char in word:

            ctr+=abs(hashmap[char]-prev)

            prev=hashmap[char]

        return ctr

        