class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = nums
        new_list.extend(nums)
        return new_list
        