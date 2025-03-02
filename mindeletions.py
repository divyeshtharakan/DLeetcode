class Solution:
    def gcd(a,b):
        if b==0:
            return a
        return gcd(b,a%b)

    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        val=numsDivide[0]
        for i in range(1,len(numsDivide)):
            if val==1:
                break
            else:
                val=gcd(val,numsDivide[i])
        for i in range(len(nums)):
            if val%nums[i]==0:
                return i
        return -1