class Solution:
    def reverseWords(self, s: List[str]) -> None:
        
        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        # Reverse the whole string
        reverse(0, len(s)-1)

        # Reverse each word
        start = 0
        
        for i in range(len(s)+1):
            if i == len(s) or s[i] == " ":
                reverse(start, i-1)
                start = i + 1