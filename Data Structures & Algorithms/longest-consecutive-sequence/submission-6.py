class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums=list(set(nums))

        nums.sort()

        maxlen,L=1,0

        #[2,3,4,5,10,20]
        
        #[0,1,2,3,4,5,6]

        if len(nums)==0:

            return len(nums)

        for R in range(1,len(nums)):

            if nums[R]-nums[R-1]!=1:

                maxlen=max(maxlen,R-L)

                L=R
            
            maxlen=max(maxlen,R-L+1)

        return maxlen



        