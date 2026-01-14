class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # 1. Is the Left character junk? Skip it.
            if not s[l].isalnum():
                l += 1
                continue # Restart the loop to check the new s[l]
            
            # 2. Is the Right character junk? Skip it.
            if not s[r].isalnum():
                r -= 1
                continue # Restart the loop to check the new s[r]
            
            # 3. Both are valid letters. Compare them.
            if s[l].lower() != s[r].lower():
                return False
            
            # 4. Match found. Move both pointers inward.
            l += 1
            r -= 1
            
        return True