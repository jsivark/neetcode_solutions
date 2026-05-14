class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #twosum with two pointers
        original_nums = [(val, i) for i, val in enumerate(nums)]
        original_nums.sort()
        left, right = 0, len(nums)-1

        while left < right:
            current_sum = original_nums[left][0] + original_nums[right][0]

            if current_sum == target:
                return sorted([original_nums[left][1], original_nums[right][1]])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
