"""3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c=0   
        l=0
        a=set()
        m=0
        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            if s[r] not in a:
                a.add(s[r])
            m=max(m,len(a))
        return m