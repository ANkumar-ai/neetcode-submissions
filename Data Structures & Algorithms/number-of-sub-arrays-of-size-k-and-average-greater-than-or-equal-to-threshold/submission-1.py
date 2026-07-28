class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        L=0
        presum=0

        ctr=0

        for R in range(len(arr)):

            presum+=arr[R]

            if R-L+1==k:

                if round(presum//k)>=threshold:

                    ctr+=1

                presum-=arr[L]
                
                L+=1



        return ctr






        