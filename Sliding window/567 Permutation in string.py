"""567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        a=[0]*26
        b=[0]*26
        for i in s1:
            a[ord(i)-97]+=1
        for i in range(len(s1)):
            b[ord(s2[i])-97]+=1
        if a==b:
            return True
        for i in range(len(s1),len(s2)):
            b[ord(s2[i-len(s1)])-97]-=1
            b[ord(s2[i])-97]+=1
            if a==b:
                return True
        return False