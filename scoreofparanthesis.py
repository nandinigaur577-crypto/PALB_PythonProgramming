class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]  # base score

        for c in s:
            if c == '(':
                stack.append(0)
            else:
                top = stack.pop()
                if top == 0:
                    score = 1
                else:
                    score = 2 * top
                stack[-1] += score

        return stack[0]
        
