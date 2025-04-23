# Time Complexity: O(k * log n), where k = number of eggs and n = number of floors
# Space Complexity: O(k), using a 1D dp array of size k+1

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[i] = max floors we can check with i eggs and current number of moves
        dp = [0] * (k + 1)
        moves = 0

        while dp[k] < n:
            moves += 1
            for eggs in range(k, 0, -1):
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1

        return moves
