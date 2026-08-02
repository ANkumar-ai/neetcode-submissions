class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i=0

        maxpro=0
        

        #[10,20,5,100]

        for R in range(1,len(prices)):

            if prices[R]<prices[i]:

                i=R

            maxpro=max(maxpro,prices[R]-prices[i])

        return maxpro
        