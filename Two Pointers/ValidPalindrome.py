class Solution:
    def isPalindrome(self, s: str) -> bool:
        #extremely rudimentary approach
        reverseStr = str[::-1]
        return reverseStr == str

        