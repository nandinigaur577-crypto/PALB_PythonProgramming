class Solution:
    def countBalanced(self, arr):
        def diff(s):
            vowels = set('aeiou')
            v = sum(1 for ch in s if ch in vowels)
            c = len(s) - v
            return v - c
        
        n = len(arr)
        prefix = 0
        count = 0
        freq = {0: 1}
        
        for i in range(n):
            prefix += diff(arr[i])
            count += freq.get(prefix, 0)
            freq[prefix] = freq.get(prefix, 0) + 1
        
        return count
