# Time Complexity: O(n^3), due to the triple nested loop
# Space Complexity: O(n^2), for the DP table

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add 1 to both ends to handle boundaries
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        
        # dp[i][j] = max coins from bursting balloons in (i, j), not including i and j
        dp = [[0] * n for _ in range(n)]

        # l is the length of subarray
        for length in range(2, n):  # length at least 2 to have (i, j) with a balloon inside
            for left in range(0, n - length):
                right = left + length
                for i in range(left + 1, right):
                    # nums[i] is the last balloon to burst in (left, right)
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]
                    )

        return dp[0][n - 1]
