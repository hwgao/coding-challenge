from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find the only pair of numbers from nums whose sum is the target
        >>> s = Solution()
        >>> s.twoSum([2, 7, 11, 15], 9)
        [0, 1]
        >>> s.twoSum([-3, 4, 3, 90], 0)
        [0, 2]
        """
        d: Dict[int, int] = {}
        for index, num in enumerate(nums):
            pair = target - num
            if pair in d:
                return [d[pair], index]
            else:
                d[num] = index
        return []
