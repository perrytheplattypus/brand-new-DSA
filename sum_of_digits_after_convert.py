class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """
        Converts a string to an integer based on alphabet positions, then performs
        a sum-of-digits transformation repeatedly k times.

        :param s: str - Input string consisting of lowercase English letters
        :param k: int - Number of transformations to perform
        :return: int - Resulting integer after k transformations
        """
        # Step 1: Convert the string to an integer representation
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Convert num_str to an integer by summing its digits
        num = sum(int(digit) for digit in num_str)
        
        # Step 2: Perform the transformation k times
        for _ in range(k - 1):
            num = sum(int(digit) for digit in str(num))
        
        return num


def main():
    # Sample test cases
    test_cases = [
        ("iiii", 1),
        ("leetcode", 2),
        ("zbax", 2)
    ]
    
    # Initialize Solution object
    solution = Solution()

    # Run each test case
    for i, (s, k) in enumerate(test_cases, 1):
        print(f"Test Case {i}: Input String: {s}, k: {k}")
        result = solution.getLucky(s, k)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
