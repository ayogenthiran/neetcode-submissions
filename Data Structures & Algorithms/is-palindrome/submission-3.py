class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l<r:
            # Skip non-alphanumeric characters from the left
            while l < r and not s[l].isalnum(): 
                l += 1
            # Skip non-alphanumeric characters from the right 
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower(): # Compare characters (convert to lowercase for case-insensitive comparison)
                return False
    
            
            l += 1
            r -= 1
        return True

    
   # def alphaNum(self, c):
      #  return(ord('A') <= ord(c) <= ord('Z') or
      #         ord('a') <= ord(c) <= ord('z') or
       #        ord('0') <= ord(c) <= ord('9'))

        