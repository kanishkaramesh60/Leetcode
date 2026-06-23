"""917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!""""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        a=""
        while i<=j:
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i].isalpha()==False:
                i+=1
            elif s[j].isalpha()==False:
                j-=1
        for i in s:
            a+=i
        return a