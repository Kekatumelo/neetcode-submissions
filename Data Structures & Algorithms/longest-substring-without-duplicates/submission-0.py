class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,longest=0,0
        seen = set()
        n=len(s)

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            w=(right-left)+1
            longest = max(longest,w)
            seen.add(s[right])
        return longest
        