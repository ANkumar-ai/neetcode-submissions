class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        L,R=0,0

        stri=""

        while L<len(word1) and R<len(word2):

            stri+=word1[L]+word2[R]

            L+=1

            R+=1

        if word1[L:]:

            return stri+word1[L:]

        if word2[R:]:

            return stri+word2[R:]

        return stri


        