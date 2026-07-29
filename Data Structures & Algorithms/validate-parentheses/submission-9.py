class Solution:
    def isValid(self, s: str) -> bool:

        dictt = {')': '(', '}': '{', ']': '['}


        stack=[]

        for char in s:

            if char in dictt:

                if dictt[char] in stack:
                    
                    if stack[-1]!=dictt[char]:

                        return False

                    else:
                        
                        stack.pop()

                else:

                    return False

            else:

                stack.append(char)

        return True if len(stack)==0 else False

            

            

            


        