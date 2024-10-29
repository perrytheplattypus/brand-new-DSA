from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        Given an array of observed dice rolls and a target mean for n + m rolls, 
        find a possible array of n missing rolls that will achieve the target mean.
        
        :param rolls: List[int] - List of observed dice rolls
        :param mean: int - Target mean for n + m rolls
        :param n: int - Number of missing rolls
        :return: List[int] - A possible array of missing rolls, or an empty list if no solution exists
        """
        m = len(rolls)             # Number of known rolls
        sum_rolls = sum(rolls)     # Sum of known rolls
        total_sum = (n + m) * mean # Required total sum for all rolls to achieve target mean
        missing_sum = total_sum - sum_rolls # Sum needed from the missing rolls
        
        # Check if the missing sum can be achieved with n rolls in the range [1, 6]
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Calculate base value and remainder for distributing the missing sum
        quotient, remainder = divmod(missing_sum, n)
        
        # Generate the list of missing rolls with values close to the mean
        return [quotient + 1] * remainder + [quotient] * (n - remainder)
