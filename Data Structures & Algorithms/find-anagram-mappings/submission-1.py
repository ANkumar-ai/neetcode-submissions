class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:


        from collections import defaultdict

        stack=defaultdict(int)

        for index,nums in enumerate(nums2):

            stack[nums]=index

        return  [stack[nums] for nums in nums1]


        