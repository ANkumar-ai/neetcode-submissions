class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L=0

        sumo=0

        minlen=float('inf')

        for R in range(len(nums)):

            sumo+=nums[R]

            while sumo>=target:

                minlen=min(minlen,R-L+1)

                sumo-=nums[L]

                L+=1

        return 0 if minlen==float('inf') else minlen






        