class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numDict:
                return [numDict[complement], i]
            else:
                numDict[nums[i]] = i
        return 