"""438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab"."""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        f=[]
        if len(p)>len(s):
            return f
        a=[0]*26
        b=[0]*26
        for i in p:
            a[ord(i)-97]+=1
        for i in range(len(p)):
            b[ord(s[i])-97]+=1
        for i in range(len(p),len(s)):
            if b==a:
                f.append(i-len(p))
            b[ord(s[i-len(p)])-97]-=1
            b[ord(s[i])-97]+=1
        if a==b:
            f.append(len(s)-len(p))
        return f