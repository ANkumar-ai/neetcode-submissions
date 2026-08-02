class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        maxlen,L,R=1,0,0

        prev=""

        while R<len(arr)-1:

            if arr[R]<arr[R+1]:

                if prev=="<":

                    L=R

                prev="<"

            elif arr[R]>arr[R+1]:

                if prev==">":

                    L=R

                prev=">"

            elif prev=="=" or arr[R]==arr[R+1]:

                if arr[R]>arr[R+1]:

                    prev=">"

                elif arr[R]<arr[R+1]:

                    prev="<"

                else:

                    prev="="

                    L=R+1

            maxlen=max(maxlen,R-L+2)

            R+=1

        return maxlen



        
        