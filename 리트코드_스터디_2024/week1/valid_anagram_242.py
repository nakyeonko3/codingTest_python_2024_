# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            flag = False
            if sorted(s) == sorted(t):
                flag = True
            return flag

if __name__ == '__main__':
    sol = Solution()
    result = sol.isAnagram('anagram', 'nagaram')
    print(result)