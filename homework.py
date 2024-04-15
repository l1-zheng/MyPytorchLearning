"""
给你一个下标从 0 开始的数组 nums ，数组中的元素都是 正 整数。
请你选出两个下标 i 和 j（i != j），且 nums[i] 的数位和 与  nums[j] 的数位和相等。
请你找出所有满足条件的下标 i 和 j ，找出并返回 nums[i] + nums[j] 可以得到的 最大值 。
"""


class Solution(object):

    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = []
        for i in nums:
            i_str = str(i)
            length = len(i_str)
            s = 0
            for idx in range(length):
                s += int(i_str[idx])
            sums.append(s)
        duplicates = [item for item in set(sums) if sums.count(item) > 1]
        if duplicates == []:
            return -1
        else:
            max_sum =[]
            for n in duplicates:
                index = [i for i, x in enumerate(sums) if x == n]
                values = []
                for i in index:
                    values.append(nums[i])
                values.sort(reverse=True)
                max_sum.append(values[0]+values[1])
            return max(max_sum)

S = Solution()
nums = [18, 43, 36, 13, 7]
p = S.maximumSum(nums)
print(p)