# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            if target - num in nums and i != nums.index(target - num):
                print(i, num)
                return [i, nums.index(target - num)]



if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,4], 6))
