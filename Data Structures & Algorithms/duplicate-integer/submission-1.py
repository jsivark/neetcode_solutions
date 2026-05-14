class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = []
        check_bin = []
        for num in nums:
            if num not in check:
                check.append(num)
                check_bin.append(False)
            else:
                check_bin.append(True)
        return any(check_bin)


            
            
                 
         