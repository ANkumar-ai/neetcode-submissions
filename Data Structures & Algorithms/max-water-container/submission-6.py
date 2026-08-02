class Solution:
    def maxArea(self, heights: List[int]) -> int:

        L,R=0,len(heights)-1

        area=0

        while L<R:

            currarea=min(heights[L],heights[R])*(R-L)

            if heights[L]<heights[R]:

                L+=1

            elif heights[R]<heights[L]:

                R-=1

            else:

                L+=1
                R-=1
            
            area=max(area,currarea)

        return area


        