class Solution:


    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {")":"(","}":"{","]":"["}
        for char in s:
            if char in mapping:
                if not stack: #to check if opening is missing
                    return False #incase we got ")", stack is empty , no opening found, if we pop in this case index error
                if stack.pop() != mapping[char]:
                    return False #to check if closing is missing

            else:
                stack.append(char)
        return len(stack)==0

        """
        stack=[{()}]
        char [ - stack state:[
        char { - stack state: [{
        char ( - stack state: [{(
        char ) - stack.pop() removes ( == mapping [")"] gives ( continue
        char } - stack.pop() removes } == mapping ["}"] gives { continue
        char ] - stack.pop() removes ] == mapping ["]"] gives [ continue
        time = o(n)
        space = o(n)
        """

    def isValidBrute(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s: #n
            s=s.replace("()","") #n * n
            s=s.replace("{}","") #n * n
            s=s.replace("[]","") #n * n
        return s==""

"""
BRUTE FORCE
"([{}])
iteration 1: ([]) (also iterte string in each iteration)
itertion  2: ()
iteration 3: ""

time complexity = n + 3 (n^2) = o(n^2)
space complexity = n chars in s =  O(n)
"""        