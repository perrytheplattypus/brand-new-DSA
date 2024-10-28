class Solution:
    def findTriplet(self, arr):
        """
        Checks if there exist three elements in the array such that the sum of
        any two of them equals the third element.

        :param arr: List[int] - List of integers to check for the triplet condition
        :return: bool - True if such a triplet exists, False otherwise
        """
        n = len(arr)
        vis = set(arr)  # Use a set to store all elements for quick lookup
        for i in range(n):
            for j in range(i + 1, n):
                # Check if the sum of arr[i] and arr[j] exists in the array
                if arr[i] + arr[j] in vis:
                    return True
        return False

def main():
    # Sample test cases
    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 3, 4]
    ]
    
    # Initialize Solution object
    solution = Solution()
    
    # Run each test case
    for i, arr in enumerate(test_cases, 1):
        print(f"Test Case {i}: Input: {arr}")
        result = solution.findTriplet(arr)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
