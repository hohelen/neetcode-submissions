class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # iterate through s, t
        # dictionary of letters from a - z 

        # if it doesnt have the same # of letters, not an anagram
        if len(s) != len(t):
            return False

        # intialize dictionaries
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if ord((s[i])) - ord('a') in s_dict:
                s_dict[ord((s[i])) - ord('a')] += 1
            else:
                s_dict[ord((s[i])) - ord('a')] = 1

            if ord((t[i])) - ord('a') in t_dict:
                t_dict[ord((t[i])) - ord('a')] += 1
            else:
                t_dict[ord((t[i])) - ord('a') ] = 1

        if s_dict == t_dict:
            return True
        return False
