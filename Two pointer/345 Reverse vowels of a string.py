"""345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"
Output: "leotcede""""

class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        a='aeiouAEIOU'
        while i<j:
            if s[i] not in a:
                i+=1
            elif s[j] not in a:
                j-=1
            elif s[i] in a and s[j] in a:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)