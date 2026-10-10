class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        integer_set = set()

        for num in nums:
            if num in integer_set:
                return True
            
            integer_set.add(num)
        return False