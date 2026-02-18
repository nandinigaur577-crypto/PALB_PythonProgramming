class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])  # reuse same element
                path.pop()  # backtrack
        
        backtrack(0, [], target)
        return result
 
