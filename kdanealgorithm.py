class Solution:
    def maxSubarraySum(self, arr):
        max_sum = arr[0]
        current_sum = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum > max_sum:
                max_sum = current_sum
                
            if current_sum < 0:
                current_sum = 0
                
        return max_sum
