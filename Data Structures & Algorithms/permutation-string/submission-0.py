from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        substrings=set()

        for i in range(0,len(s2)):

            substrings.add(s2[i:i+len(s1)])

        def is_permutation(s1, s2):
            return Counter(s1) == Counter(s2)

        for substring in substrings:

            if is_permutation(s1,substring):

                return True


        return False 

        
        