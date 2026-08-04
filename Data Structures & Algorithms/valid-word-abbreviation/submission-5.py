class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        L,R=0,0

        while L<len(word) and R<len(abbr):

            if not abbr[R].isdigit():
                
                 if word[L]!=abbr[R]:

                     return False

                 L+=1

                 R+=1

            else:
                

                if int(abbr[R])==0:

                    return False


                holder=""

                while R<len(abbr) and abbr[R].isdigit() :

                    holder+=abbr[R]

                    R+=1

                L+=int(holder)

                ctr=R+int(holder)

                holder=""

        return L == len(word) and R == len(abbr)

            

        