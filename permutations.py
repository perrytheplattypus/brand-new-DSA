class Solution:
    def permute(self, nums):
        ans = []  # List to store all permutations
        ds = []  # Temporary list to build each permutation
        freq = [False] * len(nums)  # Boolean array to track used elements
        self.permutation(nums, ds, ans, freq)
        return ans

    def permutation(self, nums, ds, ans, freq):
        # If the current permutation is the same length as nums, add it to ans
        if len(ds) == len(nums):
            ans.append(list(ds))  # Make a copy of ds and add to ans
            return

        for i in range(len(nums)):
            # If nums[i] hasn't been used in the current permutation
            if not freq[i]:
                freq[i] = True  # Mark nums[i] as used
                ds.append(nums[i])  # Add nums[i] to the current permutation
                self.permutation(nums, ds, ans, freq)  # Recurse with updated ds and freq
                ds.pop()  # Remove the last element to backtrack
                freq[i] = False  # Unmark nums[i] for the next iteration