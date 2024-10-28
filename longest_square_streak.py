from math import isqrt

class Solution:
    def longestSquareStreak(self, nums):
        """
        Finds the longest square streak in the given array.
        
        A square streak is defined as a subsequence where each element
        (after sorting) is the square of the previous element, with a minimum length of 2.
        
        :param nums: List[int] - List of integers to check for square streaks
        :return: int - The length of the longest square streak, or -1 if no streak is found
        """
        mp = {}  # Dictionary to store the longest square streak ending at each number
        nums.sort()  # Sort to ensure we can find squares in increasing order
        res = -1  # Default result if no streak is found

        for num in nums:
            sqrt = isqrt(num)  # Integer square root of num

            # Check if current number is a perfect square and if its square root exists in the map
            if sqrt * sqrt == num and sqrt in mp:
                mp[num] = mp[sqrt] + 1  # Extend the streak from the square root
                res = max(res, mp[num])  # Update the result with the longest streak found
            else:
                mp[num] = 1  # Start a new streak with the current number

        return res

def main():
    # Sample test cases
    test_cases = [
        [4, 3, 6, 16, 8, 2],
        [2, 3, 5, 6, 7]
    ]
    
    # Initialize Solution object
    solution = Solution()
    
    # Run each test case
    for i, nums in enumerate(test_cases, 1):
        print(f"Test Case {i}: Input: {nums}")
        result = solution.longestSquareStreak(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
