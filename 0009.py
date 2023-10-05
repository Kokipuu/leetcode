class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        inv_str_x = str_x[::-1]
        print(inv_str_x)
        if str_x == inv_str_x:
            return True
        else:
            return False
