class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        hashma={}

        maxnum=-1


        for num in nums:

            hashma[num] = hashma.get(num, 0) + 1

        for keys,values in hashma.items():

            if values<2:

                maxnum=max(maxnum,keys)

        return maxnum


        