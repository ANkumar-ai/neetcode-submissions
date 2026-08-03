class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        L=0

        prev=999


        for i in range(len(nums)):

            if prev!=nums[i]:

                nums[L]=nums[i]

                prev=nums[L]

                L+=1

        return L
        