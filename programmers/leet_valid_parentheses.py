"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 인
   determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

-> 괄호가 열고 닫히는 것이 valid 한지 확

솔직히 가독성 완전 별로.. 근데 졸립다..

결과
Runtime : 28 ms Memory : 14.3 MB

Runtime: 28 ms, faster than 86.02% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.3 MB, less than 63.46% of Python3 online submissions for Valid Parentheses.

(]
"""
bracket = {'(':')','[':']','{':'}'}
class Solution:
    def isValid(self, s: str) -> bool:
        s_temp = []
        i = 0
        while i<len(s):
            if(s[i]=='(' or s[i]=='[' or s[i]=='{'):
                s_temp.append(bracket[s[i]])
            elif(s[i]==')' or s[i]==']' or s[i]=='}'):
                try:
                    chk = s_temp.pop()
                except:
                    return False

                if(chk==s[i]):
                    i = i + 1
                    continue
                else:
                    return False

            i = i+1
        if(len(s_temp) != 0):
            return False

        return True





s1 = []
s1.append("()") # True
s1.append("()[]{}") # True
s1.append("(]") # False
s1.append("([)]") # False
s1.append("{[]}") #True

d = Solution()
for i in range(len(s1)):
    b = d.isValid(s1[i])
    print(b)