class Solution:
    def countElements(self, arr: List[int]) -> int:

        hass=set(arr)

        ctr=0


        for i in range(len(arr)):

            if arr[i]+1 in hass:

                ctr+=1
        
        return ctr


        