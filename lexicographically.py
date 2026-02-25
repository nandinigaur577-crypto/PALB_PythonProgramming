class Solution:
    def maxSubseq(self, s, k):
        stack = []
        remove = k
        
        for ch in s:
            while remove > 0 and stack and stack[-1] < ch:
                stack.pop()
                remove -= 1
            stack.append(ch)
        
        # If removals still left, remove from end
        if remove > 0:
            stack = stack[:-remove]
        
        return "".join(stack)
