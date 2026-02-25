class Solution:
    def search(self, txt, pat):
        from collections import Counter
        
        k = len(pat)
        if k > len(txt):
            return False
        
        pat_count = Counter(pat)
        window_count = Counter(txt[:k])
        
        if window_count == pat_count:
            return True
        
        for i in range(k, len(txt)):
            window_count[txt[i]] += 1
            window_count[txt[i - k]] -= 1
            
            if window_count[txt[i - k]] == 0:
                del window_count[txt[i - k]]
            
            if window_count == pat_count:
                return True
        
        return False
