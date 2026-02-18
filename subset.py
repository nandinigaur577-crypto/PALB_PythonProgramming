lass Solution(object):
    def subsets(self, nums):
        result = []
        
        def backtrack(start, path):
            # Add current subset
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # undo choice
        
        backtrack(0, [])
        return result
