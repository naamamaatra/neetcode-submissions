class Solution:
    def isPalindrome(self, s: str) -> bool:
        right=0
        left=len(s)-1
        while left<right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right+=1
            else:
                if(s[left].lower()!=s[right].lower()):
                    return False
                i+=1
                j+=1
        return True