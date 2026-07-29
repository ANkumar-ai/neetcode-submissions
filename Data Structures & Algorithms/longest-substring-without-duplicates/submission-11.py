class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        "abba"

        L=0

        maxlen=0

        mape={}

        for R in range(len(s)):

            if s[R] in mape and mape[s[R]]>=L:

                L=mape[s[R]]+1

                mape.pop(s[R])

            mape[s[R]]=R

            maxlen=max(maxlen,R-L+1)

        return maxlen

            






        