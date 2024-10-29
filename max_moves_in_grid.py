from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        """
        Finds the maximum number of moves possible in a grid starting from any cell
        in the first column. Moves can only proceed to the right if each subsequent cell
        has a greater value than the current cell.

        :param grid: List[List[int]] - 2D grid of positive integers
        :return: int - Maximum number of moves possible
        """
        m = len(grid)    # number of rows
        n = len(grid[0]) # number of columns
        res = 0
        dp = [0] * m  # Stores the maximum moves possible for each cell in the current column

        # Iterate through each column from left to right
        for j in range(1, n):
            leftTop = 0
            found = False

            for i in range(m):
                cur = -1  # Initialize current cell's moves as unreachable
                nxtLeftTop = dp[i]  # Store dp[i] for the next row's leftTop update

                # Check possible moves from top-left, left, and bottom-left cells
                if i - 1 >= 0 and leftTop != -1 and grid[i][j] > grid[i-1][j-1]:
                    cur = max(cur, leftTop + 1)
                if dp[i] != -1 and grid[i][j] > grid[i][j-1]:
                    cur = max(cur, dp[i] + 1)
                if i + 1 < m and dp[i+1] != -1 and grid[i][j] > grid[i+1][j-1]:
                    cur = max(cur, dp[i+1] + 1)

                dp[i] = cur  # Update dp for the current cell
                found = found or (dp[i] != -1)  # Update found flag if reachable
                leftTop = nxtLeftTop  # Update leftTop for next row

            if not found:
                break
            res = j  # Update result to the current column index if reachable

        return res


def main():
    # Sample test cases
    test_cases = [
        [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]],
        [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
    ]
    
    # Initialize Solution object
    solution = Solution()

    # Run each test case
    for i, grid in enumerate(test_cases, 1):
        print(f"Test Case {i}: Input Grid: {grid}")
        result = solution.maxMoves(grid)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
