from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[k-1]


if __name__ == '__main__':
    solution = Solution()
    result = solution.findKthLargest([1,2,3,4,5],3)
    print(result)