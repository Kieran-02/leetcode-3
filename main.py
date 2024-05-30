class Solution:

    def lengthOfLongestSubstring(self, stringToCheck: str) -> int:
        maxLength = 0
        charMap = {}
        left = 0

        for right in range(len(stringToCheck)):
            if stringToCheck[right] not in charMap or charMap[stringToCheck[right]] < left:
                charMap[stringToCheck[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[stringToCheck[right]] + 1
                charMap[stringToCheck[right]] = right

        return maxLength

s = Solution
print(s.lengthOfLongestSubstring(s,'abbbbbabc'))