class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        L,R=0,0

        ctr=0

        while L<len(s) and R<len(t):

            if s[L]==t[R]:

                L+=1

                ctr+=1

            R+=1

        return ctr==len(s)


        