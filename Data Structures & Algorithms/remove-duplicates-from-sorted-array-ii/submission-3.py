class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

      count,L,R=1,0,0

      while R<len(nums):

         prev=nums[R]

         while R+1<len(nums) and nums[R]==nums[R+1]:

            count+=1

            R+=1

         count=min(2,count)

         for i in range(L,L+count):

            nums[i]=prev

            L+=1

         count=1

         R+=1

      return L
        