class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        flag = False
        for num in  nums:
            print(num)
            if num in seen:
                flag = True
        return flag





sol = Solution()
result = sol.containsDuplicate([1,2,3,4])
print(result)
