class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leftPointer = 1

        for rightPointer in range(1,len(nums)):
           if nums[rightPointer] != nums[rightPointer - 1]:
            nums[leftPointer] = nums[rightPointer]
            leftPointer += 1
        return leftPointer
