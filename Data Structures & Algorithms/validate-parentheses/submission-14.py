class Solution:
    def isValid(self, s: str) -> bool:

        sta={"]":"[","}":"{",")":"("}

        stack=[]

        if len(s)<=1:

            return False

        for char in s:

            if  char in sta:
                
                if stack and stack[-1]!=sta[char] or len(stack)==0:

                    return False

                stack.pop()

            else:
                
                stack.append(char)

        return len(stack)==0 








        