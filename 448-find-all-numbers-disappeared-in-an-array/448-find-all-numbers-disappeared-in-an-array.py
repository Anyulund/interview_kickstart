class Solution:
        def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
            length = len(nums)
            nums = set(nums)
            ans = []

            for n in range(1, length+1):
                if n not in nums:
                    ans.append(n)

            return ans