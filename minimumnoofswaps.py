class Solution:
    def minSwaps(self, s1, s2):
        count10 = 0
        count01 = 0
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == '1':
                    count10 += 1
                else:
                    count01 += 1
        
        if (count10 + count01) % 2 != 0:
            return -1
        
        return (count10 // 2) + (count01 // 2) + 2 * (count10 % 2)
