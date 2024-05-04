# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        flag = False
        for num in nums:
            if num in seen:
                flag = True
            seen[num] = num
        return flag

if __name__ == '__main__':
    sol = Solution()
    result = sol.containsDuplicate([1,2,3,4])
    print(result)
