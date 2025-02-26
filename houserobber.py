class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1, prev2 = 0, 0  # prev1 stores max profit up to i-1, prev2 up to i-2

        for num in nums:
            temp = prev1  # Store previous max before updating
            prev1 = max(prev1, prev2 + num)  # Either rob current house or skip
            prev2 = temp  # Move prev1 to prev2 for next iteration

        return prev1