'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
'''


class Solution(object):

    def __init__(self):
        self.index = 0

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx = [i for i, x in enumerate(nums) if x == target]
        if not idx:
            for i in nums:
                if i >= target:
                    self.index = nums.index(i)
                    break
                else:
                    self.index = len(nums)
        else:
            self.index = idx[0]
        return self.index


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_searchInsert(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 0), 0)


if __name__ == '__main__':
    unittest.main()