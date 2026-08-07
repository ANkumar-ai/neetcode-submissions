class Solution:
    def confusingNumber(self, n: int) -> bool:

        liss={0:0,1:1,6:9,8:8,9:6}

        sr=""

        for num in  str(n):

            if int(num) not in liss:

                return False

            else:

                sr+=str(liss[int(num)])

        return sr[::-1]!=str(n)

