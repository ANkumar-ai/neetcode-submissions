class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        L=0

        suml=0

        ctr=0

        for R in range(len(arr)):

            suml+=arr[R]

            if R-L+1==k:

                if suml//k>=threshold:

                    ctr+=1

                suml-=arr[L]

                L+=1
            
        return ctr


        