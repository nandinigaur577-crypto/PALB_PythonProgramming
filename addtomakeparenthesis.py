class Solution:
    def minParentheses(self, s):
        balance = 0
        insertions = 0
        
        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ch == ')'
                if balance > 0:
                    balance -= 1
                else:
                    insertions += 1
        
        return insertions + balance
