from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Simulates a robot moving in an infinite grid according to specified commands and obstacles.

        :param commands: List[int] - List of movement commands (-2: turn left, -1: turn right, k: move forward k units)
        :param obstacles: List[List[int]] - List of obstacle coordinates on the grid
        :return: int - Maximum squared Euclidean distance the robot reaches from the origin
        """
        # Direction mappings for 'N', 'E', 'S', 'W'
        directions = ['N', 'E', 'S', 'W']
        current_direction = 0  # Start facing north
        x, y = 0, 0  # Starting position at the origin
        max_distance = 0
        
        # Convert obstacles list to a set for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        # Process each command
        for command in commands:
            if command == -1:  # Turn right
                current_direction = (current_direction + 1) % 4
            elif command == -2:  # Turn left
                current_direction = (current_direction - 1) % 4
            else:  # Move forward
                # Determine direction and attempt to move one step at a time
                for _ in range(command):
                    if directions[current_direction] == 'N' and (x, y + 1) not in obstacle_set:
                        y += 1
                    elif directions[current_direction] == 'E' and (x + 1, y) not in obstacle_set:
                        x += 1
                    elif directions[current_direction] == 'S' and (x, y - 1) not in obstacle_set:
                        y -= 1
                    elif directions[current_direction] == 'W' and (x - 1, y) not in obstacle_set:
                        x -= 1
                    else:
                        break  # Stop moving if an obstacle is encountered
                    
                # Update the maximum distance reached
                max_distance = max(max_distance, x**2 + y**2)
        
        return max_distance


# Example usage and test cases
def main():
    solution = Solution()
    test_cases = [
        ([4, -1, 3], []),
        ([4, -1, 4, -2, 4], [[2, 4]]),
        ([6, -1, -1, 6], [[0, 0]])
    ]
    
    for i, (commands, obstacles) in enumerate(test_cases, 1):
        result = solution.robotSim(commands, obstacles)
        print(f"Test Case {i}: Commands: {commands}, Obstacles: {obstacles} -> Output: {result}")


if __name__ == "__main__":
    main()
