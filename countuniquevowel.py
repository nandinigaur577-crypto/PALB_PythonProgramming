class Solution:
    def vowelCount(self, s):
        from math import factorial
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        freq = {}
        
        for ch in s:
            if ch in vowels:
                freq[ch] = freq.get(ch, 0) + 1
        
        if not freq:
            return 0
        
        total_choices = 1
        for count in freq.values():
            total_choices *= count
        
        return total_choices * factorial(len(freq))
