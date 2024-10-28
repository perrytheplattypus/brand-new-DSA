class Solution:
    def removeDuplicates(self, arr):
        """
        Removes duplicate elements from the array while preserving the order of first occurrences.

        :param arr: List[int] - List of positive integers with potential duplicates
        :return: List[int] - List of integers with duplicates removed
        """
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return res

def main():
    # Sample test cases
    test_cases = [
        [2, 2, 3, 3, 7, 5],
        [2, 2, 5, 5, 7, 7],
        [8, 7]
    ]
   
    # Initialize Solution object
    solution = Solution()
    
    # Run each test case
    for i, arr in enumerate(test_cases, 1):
        print(f"Test Case {i}: Input: {arr}")
        result = solution.removeDuplicates(arr)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
