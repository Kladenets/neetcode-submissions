class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams must be the same length
        if len(s) != len(t):
            return False

        # make s positive, t negative, track count of letters in an array, 
        # check for non zero counts after loop
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1

        for num in counts:
            if num != 0:
                return False

        return True
