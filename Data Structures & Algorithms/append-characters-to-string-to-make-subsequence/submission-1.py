class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        L,R=0,0

        while L<len(s) and R<len(t):

            if t[R]==s[L]:

                R+=1

            L+=1

        return len(t[R:]) if t[R:] else 0
        