class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap={}


        for i,nums in enumerate(nums):

            if target-nums in hashmap:

                return [hashmap[target-nums],i]

            hashmap[nums]=i
        






        