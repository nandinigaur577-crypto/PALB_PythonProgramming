class Solution:
    def minDifference(self, arr):
        def to_seconds(t):
            h, m, s = map(int, t.split(':'))
            return h * 3600 + m * 60 + s

        times = [to_seconds(t) for t in arr]
        times.sort()

        min_diff = float('inf')

        # check adjacent differences
        for i in range(1, len(times)):
            min_diff = min(min_diff, times[i] - times[i-1])

        # check wrap-around difference
        seconds_in_day = 24 * 3600
        wrap_diff = seconds_in_day - times[-1] + times[0]
        min_diff = min(min_diff, wrap_diff)

        return min_diff
